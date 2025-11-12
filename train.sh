#!/bin/bash

python src/DynamicLimit-Exp.py   --train_file data/10Mf/train/10Mf.txt --validation_file data/10Mf/dev/10Mf.txt  --tokenizer_file gpt2_mini_baby_10Mf_32768_76/tokenizer.json  --output_dir output_dynamic_10Mf_20_32 --num_train_epochs 20 --per_device_train_batch_size 128 --max_seq_length 128

python src/NoLimit.py   --train_file data/10Mf/train/10Mf.txt --validation_file data/10Mf/dev/10Mf.txt  --tokenizer_file gpt2_mini_baby_10Mf_32768_76/tokenizer.json  --output_dir output_linear_10Mf_20_32 --num_train_epochs 20 --per_device_train_batch_size 128 --max_seq_length 128

