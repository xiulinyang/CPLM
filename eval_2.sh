#!/bin/bash

python eval_bench.py xiulinyang/linear_dyck_chunk_96 --eval_dataset posh
python eval_bench.py xiulinyang/linear_dyck_chunk_128 --eval_dataset posh
python eval_bench.py xiulinyang/linear_dyck_chunk_0 --eval_dataset posh

python eval_bench.py xiulinyang/linear_dyck_chunk_96 --eval_dataset zorro
python eval_bench.py xiulinyang/linear_dyck_chunk_128 --eval_dataset zorro
python eval_bench.py xiulinyang/linear_dyck_chunk_0 --eval_dataset zorro


python eval_bench.py xiulinyang/linear_dyck_chunk_96 --eval_dataset scamp_plausible
python eval_bench.py xiulinyang/linear_dyck_chunk_128 --eval_dataset scamp_plausible
python eval_bench.py xiulinyang/linear_dyck_chunk_0 --eval_dataset scamp_plausible

python eval_bench.py xiulinyang/linear_dyck_chunk_96 --eval_dataset blimp
python eval_bench.py xiulinyang/linear_dyck_chunk_128 --eval_dataset blimp
python eval_bench.py xiulinyang/linear_dyck_chunk_0 --eval_dataset blimp

python eval_bench.py xiulinyang/linear_only_chunk_96 --eval_dataset posh
python eval_bench.py xiulinyang/linear_only_chunk_128 --eval_dataset posh
python eval_bench.py xiulinyang/linear_only_chunk_0 --eval_dataset posh

python eval_bench.py xiulinyang/linear_only_chunk_96 --eval_dataset zorro
python eval_bench.py xiulinyang/linear_only_chunk_128 --eval_dataset zorro
python eval_bench.py xiulinyang/linear_only_chunk_0 --eval_dataset zorro


python eval_bench.py xiulinyang/linear_only_chunk_96 --eval_dataset scamp_plausible
python eval_bench.py xiulinyang/linear_only_chunk_128 --eval_dataset scamp_plausible
python eval_bench.py xiulinyang/linear_only_chunk_0 --eval_dataset scamp_plausible

python eval_bench.py xiulinyang/linear_only_chunk_96 --eval_dataset blimp
python eval_bench.py xiulinyang/linear_only_chunk_128 --eval_dataset blimp
python eval_bench.py xiulinyang/linear_only_chunk_0 --eval_dataset blimp

#python eval_bench.py xiulinyang/linear_dyck_chunk_96 --eval_dataset blimp
#python eval_bench.py xiulinyang/linear_dyck_chunk_128 --eval_dataset blimp
#python eval_bench.py xiulinyang/linear_dyck_chunk_0 --eval_dataset blimp

#python eval_bench.py xiulinyang/linear_chunk_96 --eval_dataset posh
#python eval_bench.py xiulinyang/linear_chunk_128 --eval_dataset posh

#python eval_bench.py xiulinyang/linear_chunk_96 --eval_dataset zorro
#python eval_bench.py xiulinyang/linear_chunk_128 --eval_dataset zorro

#python eval_bench.py xiulinyang/linear_chunk_96 --eval_dataset scamp_plausible
#python eval_bench.py xiulinyang/linear_chunk_128 --eval_dataset scamp_plausible

#python eval_bench.py xiulinyang/linear_chunk_96 --eval_dataset blimp
#python eval_bench.py xiulinyang/linear_chunk_128 --eval_dataset blimp
