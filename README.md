# Critical Period-inspired Language Model (CPLM)
This repository provides code for training the Critical Period-inspired Language Model (CPLM).

>[Masato Mita, Ryo Yoshida, Yohei Oseki. Developmentally-plausible Working Memory Shapes a Critical Period for Language Acquisition. ACL2025.](https://aclanthology.org/2025.acl-long.462/)



# Installation
This repository uses a customized version of [Hugging Face Transformers](https://github.com/huggingface/transformers) (with custom modules like `modeling_gpt2_alibi_exponential.py`).  
Please follow these steps to install the environment properly.

## 0. Prerequirments
- python==3.10.12
- uv==0.6.3
- torch==1.12.1+cu113


## 1. Clone this repository

```bash
git clone https://github.com/osekilab/CPLM.git
cd CPLM
```
## 2. Create a virtual environment

```bash
uv venv .venv
source .venv/bin/activate
uv pip sync --requirement uv.lock
```

## 3. Install the customized transformers in editable mode
```bash
uv pip install -e ./transformers
```

# Run
```bash
python src/DynamicLimit-Exp.py \
  --train_file path/to/train.txt \
  --tokenizer_file path/to/tokenizer.json \
  --output_dir output/
```
For example:
```bash
python src/DynamicLimit-Exp.py \
  --train_file data/sentences_with_age-ordered.txt \
  --tokenizer_file childs_tokenizer/tokenizer.json \
  --per_device_train_batch_size 512 \
  --output_dir output/
```



# Citation
If you use our code for your work, please cite:

```
@inproceedings{mita-etal-2025-developmentally,
    title = "Developmentally-plausible Working Memory Shapes a Critical Period for Language Acquisition",
    author = "Mita, Masato  and
      Yoshida, Ryo  and
      Oseki, Yohei",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.462/",
    pages = "9386--9399",
    ISBN = "979-8-89176-251-0",
    abstract = "Large language models possess general linguistic abilities but acquire language less efficiently than humans. This study proposes a method for integrating the developmental characteristics of working memory during the critical period, a stage when human language acquisition is particularly efficient, into the training process of language models. The proposed method introduces a mechanism that initially constrains working memory during the early stages of training and gradually relaxes this constraint in an exponential manner as learning progresses. Targeted syntactic evaluation shows that the proposed method outperforms conventional methods without memory constraints or with static memory constraints. These findings not only provide new directions for designing data-efficient language models but also offer indirect evidence supporting the role of the developmental characteristics of working memory as the underlying mechanism of the critical period in language acquisition."
}
```

