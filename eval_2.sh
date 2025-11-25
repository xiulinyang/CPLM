#!/bin/bash

python eval_bench.py xiulinyang/dynamic_dyck_96 --eval_dataset posh
python eval_bench.py xiulinyang/dynamic_dyck_128 --eval_dataset posh
python eval_bench.py xiulinyang/dynamic_dyck_0 --eval_dataset posh

python eval_bench.py xiulinyang/dynamic_dyck_96 --eval_dataset zorro
python eval_bench.py xiulinyang/dynamic_dyck_128 --eval_dataset zorro
python eval_bench.py xiulinyang/dynamic_dyck_0 --eval_dataset zorro


python eval_bench.py xiulinyang/dynamic_dyck_96 --eval_dataset scamp_plausible
python eval_bench.py xiulinyang/dynamic_dyck_128 --eval_dataset scamp_plausible
python eval_bench.py xiulinyang/dynamic_dyck_0 --eval_dataset scamp_plausible

python eval_bench.py xiulinyang/dynamic_dyck_96 --eval_dataset blimp
python eval_bench.py xiulinyang/dynamic_dyck_128 --eval_dataset blimp
python eval_bench.py xiulinyang/dynamic_dyck_0 --eval_dataset blimp

#python eval_bench.py xiulinyang/dynamic_dyck_chunk_96 --eval_dataset blimp
#python eval_bench.py xiulinyang/dynamic_dyck_chunk_128 --eval_dataset blimp
#python eval_bench.py xiulinyang/dynamic_dyck_chunk_0 --eval_dataset blimp

#python eval_bench.py xiulinyang/dynamic_chunk_96 --eval_dataset posh
#python eval_bench.py xiulinyang/dynamic_chunk_128 --eval_dataset posh

#python eval_bench.py xiulinyang/dynamic_chunk_96 --eval_dataset zorro
#python eval_bench.py xiulinyang/dynamic_chunk_128 --eval_dataset zorro

#python eval_bench.py xiulinyang/dynamic_chunk_96 --eval_dataset scamp_plausible
#python eval_bench.py xiulinyang/dynamic_chunk_128 --eval_dataset scamp_plausible

#python eval_bench.py xiulinyang/dynamic_chunk_96 --eval_dataset blimp
#python eval_bench.py xiulinyang/dynamic_chunk_128 --eval_dataset blimp
