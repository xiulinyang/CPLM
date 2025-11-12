---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: gpt2_mini_baby_10Mf_32768_76
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2_mini_baby_10Mf_32768_76

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 4.4300
- Accuracy: 0.2997

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 76
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 40000
- training_steps: 100000

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 5.934         | 2.2   | 2000  | 6.5359          | 0.1723   |
| 4.3434        | 4.39  | 4000  | 5.7227          | 0.2059   |
| 4.0422        | 6.59  | 6000  | 5.3931          | 0.2165   |
| 3.8918        | 8.78  | 8000  | 5.1812          | 0.2272   |
| 3.7238        | 10.98 | 10000 | 5.0201          | 0.2455   |
| 3.593         | 13.17 | 12000 | 4.8982          | 0.2586   |
| 3.4887        | 15.37 | 14000 | 4.7813          | 0.2668   |
| 3.4028        | 17.56 | 16000 | 4.6885          | 0.2753   |
| 3.3367        | 19.76 | 18000 | 4.6320          | 0.2808   |
| 3.2726        | 21.95 | 20000 | 4.5714          | 0.2867   |
| 3.2202        | 24.15 | 22000 | 4.5151          | 0.2911   |
| 3.1682        | 26.34 | 24000 | 4.4626          | 0.2945   |
| 3.1246        | 28.54 | 26000 | 4.4451          | 0.2979   |
| 3.0849        | 30.74 | 28000 | 4.4300          | 0.2997   |
| 3.0504        | 32.93 | 30000 | 4.4026          | 0.2999   |
| 3.0149        | 35.13 | 32000 | 4.4306          | 0.3019   |
| 2.981         | 37.32 | 34000 | 4.4283          | 0.3013   |
| 2.955         | 39.52 | 36000 | 4.4351          | 0.3013   |
| 2.9297        | 41.71 | 38000 | 4.4214          | 0.3035   |
| 2.9027        | 43.91 | 40000 | 4.4378          | 0.3027   |
| 2.8685        | 46.1  | 42000 | 4.4750          | 0.3020   |
| 2.8387        | 48.3  | 44000 | 4.4777          | 0.3019   |


### Framework versions

- Transformers 4.30.2
- Pytorch 2.9.0+cu128
- Datasets 4.1.1
- Tokenizers 0.13.3
