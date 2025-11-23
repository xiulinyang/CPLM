#!/bin/bash


python src/DynamicLimit-Exp.py  --train_file data/10Mf/train/10Mf.txt --validation_file data/10Mf/dev/10Mf.txt  --tokenizer_file gpt2_mini_baby_10Mf_32768_53/tokenizer.json --output_dir dynamic_dyck --num_train_epochs 10 --per_device_train_batch_size 64 --max_seq_length 128 --resume_from_checkpoint dynamic_dyck-pretrain/epoch_0 

#python src/NoLimit.py  --train_file data/10Mf/train/10Mf.txt --validation_file data/10Mf/dev/10Mf.txt  --tokenizer_file gpt2_mini_baby_10Mf_32768_53/tokenizer.json --output_dir linear_dyck --num_train_epochs 10 --per_device_train_batch_size 64 --max_seq_length 128 --resume_from_checkpoint dyck-pretrain/epoch_0

#python src/DynamicLimit-Exp.py  --train_file data/10Mf/train/10Mf.txt --validation_file data/10Mf/dev/10Mf.txt  --tokenizer_file gpt2_mini_baby_10Mf_32768_53/tokenizer.json --output_dir dynamic_only --num_train_epochs 10 --per_device_train_batch_size 64 --max_seq_length 128 

#python src/NoLimit.py  --train_file data/10Mf/train/10Mf.txt --validation_file data/10Mf/dev/10Mf.txt  --tokenizer_file gpt2_mini_baby_10Mf_32768_53/tokenizer.json --output_dir linear_only --num_train_epochs 10 --per_device_train_batch_size 64 --max_seq_length 128


