#!/bin/bash



python eval.py --model_dir output_linear_10Mf_20 --eval_dataset zorro --device cuda --tokenizer_dir output_linear_10Mf_20
python eval.py --model_dir output_linear_10Mf_20 --eval_dataset posh --device cuda --tokenizer_dir output_linear_10Mf_20
python eval.py --model_dir output_linear_10Mf_20 --eval_dataset blimp --device cuda --tokenizer_dir output_linear_10Mf_20
python eval.py --model_dir output_linear_10Mf_20 --eval_dataset scamp_plausible --device cuda --tokenizer_dir output_linear_10Mf_20
