#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
from glob import glob
from pathlib import Path

import torch
import pandas as pd
from tqdm import tqdm

#ifrom transformers.models.gpt2.modeling_gpt2_alibi_exponential import GPT2LMHeadModel

from transformers.models.gpt2.modeling_gpt2 import GPT2LMHeadModel
from transformers import AutoTokenizer

def read_data(data_path, dataset_name):
    test_set = {}

    if dataset_name in ["zorro", "posh"]:
        phenomenon_paths = glob(f"{data_path}/*.txt")
        for p in tqdm(phenomenon_paths, desc=f"Loading {dataset_name}"):
            phenomenon = Path(p).stem
            sentences = Path(p).read_text().strip().split("\n")
            if "strict" in p:
                sent_pair = [
                    (
                        sentences[i],
                        sentences[i + 1],
                        sentences[i + 2],
                        sentences[i + 3],
                        sentences[i + 4],
                        sentences[i + 5],
                    )
                    for i in range(0, len(sentences), 6)
                ]
            else:
                sent_pair = [(sentences[i], sentences[i + 1]) for i in range(0, len(sentences), 2)]
            test_set[phenomenon] = sent_pair

    elif dataset_name in ["blimp"]:
        phenomenon_paths = glob(f"{data_path}/*.jsonl")
        for p in tqdm(phenomenon_paths, desc="Loading blimp"):
            phenomenon_n = Path(p).stem
            phenomenon = pd.read_json(p, lines=True).to_dict(orient="records")
            sent_pair = [(x["sentence_bad"], x["sentence_good"]) for x in phenomenon]
            test_set[phenomenon_n] = sent_pair

    elif dataset_name in ["scamp_plausible", "scamp_implausible"]:
        phenomenon_paths = glob(f"{data_path}/*.tsv")
        for p in tqdm(phenomenon_paths, desc="Loading scamp"):
            phenomenon = Path(p).stem
            lines = Path(p).read_text().strip().split("\n")
            sent_pair = [(x.split("\t")[1], x.split("\t")[0]) for x in lines]
            test_set[phenomenon] = sent_pair

    else:
        raise ValueError(
            f"{dataset_name} is not available! Choose from: "
            f"[blimp, scamp_plausible, scamp_implausible, zorro, posh]"
        )
    return test_set

class SimpleScorer:
    def __init__(self, model_dir, device="cpu", tokenizer_dir=None):
        self.device = torch.device(device)
        tok_src = tokenizer_dir if tokenizer_dir else model_dir
        self.tok = AutoTokenizer.from_pretrained(tok_src)

        if self.tok.pad_token is None:
            if "[PAD]" in self.tok.get_vocab():
                self.tok.pad_token = "[PAD]"
            else:
                self.tok.pad_token = self.tok.eos_token or self.tok.unk_token

        self.bos_id = None
        if "[BOS]" in self.tok.get_vocab():
            self.bos_id = self.tok.convert_tokens_to_ids("[BOS]")
        elif self.tok.bos_token_id is not None:
            self.bos_id = self.tok.bos_token_id

        self.model = GPT2LMHeadModel.from_pretrained(model_dir)
        self.model.to(self.device).eval()

    @torch.no_grad()
    def sequence_score(self, sent_list, max_length=None):
        """
        输入: list[str] -> 输出: list[float]（每句总 NLL，自然对数）
        计分仅覆盖“原始 token”（add_special_tokens=False），与 num_tokens 统计一致。
        """
        enc = self.tok(
            list(sent_list),
            add_special_tokens=False,
            return_tensors="pt",
            padding=True,
            truncation=(max_length is not None),
            max_length=max_length,
        )
        ids = enc["input_ids"].to(self.device)        # [B, L]
        mask = enc["attention_mask"].to(self.device)  # [B, L]

        inputs = ids.clone()
        inputs[:, 1:] = ids[:, :-1]
        fill_id = self.bos_id if self.bos_id is not None else self.tok.pad_token_id
        inputs[:, 0] = fill_id

        in_mask = mask.clone()
        in_mask[:, 1:] = mask[:, :-1]
        in_mask[:, 0] = 1

        out = self.model(input_ids=inputs, attention_mask=in_mask)
        log_probs = torch.log_softmax(out.logits, dim=-1)          # [B, L, V]
        labels = ids
        token_logp = log_probs.gather(-1, labels.unsqueeze(-1)).squeeze(-1)  # [B, L]
        token_logp = token_logp * mask
        nll = -(token_logp.sum(dim=-1))  # [B]
        ntoks = mask.sum(dim=-1) 

        sent_ppl = torch.exp(nll / ntoks) 
        return [x.item() for x in sent_ppl]

def eval_sent_pair(ilm_model, tokenizer, test_set):
    results = {}
    distributions = {}
    for phe, sents in tqdm(test_set.items(), desc="Evaluating"):
        correct = 0
        distribution = []
        for sent in sents:
            sent = list(sent)
            if "strict" in phe:
                num_tokens = [
                    len(tokenizer.encode(sent[i], add_special_tokens=False))
                    for i in range(len(sent))
                ]
                scores = ilm_model.sequence_score(sent)  # NLL 列表
                ppls = [(i, x / y) for i, (x, y) in enumerate(zip(scores, num_tokens))]
                ppls = sorted(ppls, key=lambda x: x[1])
                if ppls[0][0] == 5:
                    correct += 1
                distribution.append(ppls)
            else:
                ppl0, ppl1 = ilm_model.sequence_score(sent)
                distribution.append([(0, ppl0), (1, ppl1)])
                if ppl0 > ppl1:
                    correct += 1
        acc = correct / len(sents) if len(sents) > 0 else float("nan")
        results[phe] = acc
        distributions[phe] = distribution
        print(phe, acc)
    return results, distributions

def main():
    ap = argparse.ArgumentParser("eval custom GPT-2 (ALiBi exponential) without minicons")
    ap.add_argument("--model_dir", type=str, required=True, help="本地模型或单个 checkpoint 目录")
    ap.add_argument("--eval_dataset", type=str, default="posh",
                    help="posh / zorro / blimp / scamp_plausible / scamp_implausible")
    ap.add_argument("--device", type=str, default="cpu", choices=["cpu", "cuda"])
    ap.add_argument("--tokenizer_dir", type=str, default=None, help="若 tokenizer 不在 model_dir，可显式指定")
    ap.add_argument("--max_length", type=int, default=None, help="可选，评分时截断长度")
    args = ap.parse_args()

    os.makedirs(f"{args.eval_dataset}_results", exist_ok=True)
    test = read_data(f"{args.eval_dataset}", args.eval_dataset)

    tok_src = args.tokenizer_dir if args.tokenizer_dir else args.model_dir
    tokenizer = AutoTokenizer.from_pretrained(tok_src)
    checkpoints = glob(f'{args.model_dir}/epoch*')
    print(checkpoints)
    for checkpoint in checkpoints:
        scorer = SimpleScorer(f'{checkpoint}', device=args.device, tokenizer_dir=args.tokenizer_dir)
        acc, dist = eval_sent_pair(scorer, tokenizer, test)
        epoch = checkpoint.split('/')[-1]
        tag = Path(args.model_dir).namec
        out_dir = f"{args.eval_dataset}_results"
        pd.DataFrame({"best": acc}).to_csv(f"{out_dir}/results_{tag}_{checkpoint}.csv")
        pd.DataFrame(dist).to_csv(f"{out_dir}/distributions_{tag}_{checkpoint}.csv")
        print("Done.")

if __name__ == "__main__":
    main()
