# Critical Period-inspired Language Model (CPLM)
This repository provides code for training the Critical Period-inspired Language Model (CPLM).

>Masato Mita, Ryo Yoshida, Yohei Oseki. Developmentally-plausible Working Memory Shapes a Critical Period for Language Acquisition. ACL2025. (To appear)  



# Installation
This repository uses a customized version of Hugging Face Transformers (with custom modules like `modeling_gpt2_alibi_exponential.py`).  
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
@misc{mita2025developmentallyplausibleworkingmemoryshapes,
      title={Developmentally-plausible Working Memory Shapes a Critical Period for Language Acquisition},
      author={Masato Mita and Ryo Yoshida and Yohei Oseki},
      year={2025},
      eprint={2502.04795},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.04795},
}
```

