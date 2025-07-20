# train-custom_tokenizer.py

import argparse
from tokenizers import ByteLevelBPETokenizer

def main(args):
    # ローカルデータを使ってトークナイザーを訓練
    tokenizer = ByteLevelBPETokenizer()

    # トークナイザーの訓練
    tokenizer.train(files=[args.train_file], vocab_size=args.vocab_size, min_frequency=args.min_frequency, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ])

    # 訓練済みのトークナイザーを保存
    tokenizer.save_model(args.output_dir)
    print(f"Tokenizer saved to {args.output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a custom Byte-Pair Encoding (BPE) tokenizer.")
    parser.add_argument("--train_file", type=str, required=True, help="Path to the training text file.")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save the trained tokenizer.")
    parser.add_argument("--vocab_size", type=int, default=50257, help="Vocabulary size for the tokenizer.")
    parser.add_argument("--min_frequency", type=int, default=2, help="Minimum frequency for tokens to be included in the vocabulary.")

    args = parser.parse_args()
    main(args)