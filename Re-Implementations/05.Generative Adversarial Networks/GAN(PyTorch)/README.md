# GAN-PyTorch

- This repository contains an **PyTorch** reimplementation of the paper [**Generative Adversarial Networks**](http://arxiv.org/pdf/1406.2661).

## Table of contents

- [GAN-PyTorch](#gan-pytorch)
  - [Overview](#overview)
    - [Table of contents](#table-of-contents)
    - [Download weights](#download-weights)
    - [Test](#test)
    - [Train](#train)
    - [Contributing](#contributing)
    - [Credit](#credit)
      - [Generative Adversarial Networks](#generative-adversarial-networks)

### Download weights

- [Google Driver](https://drive.google.com/file/d/1rt0iZbWXTZBCh97x3eK_lbTLshnw9Tqp/view?usp=sharing)
- [Baidu Driver](https://pan.baidu.com/s/1Qa50gFnp681g8ElOXrbTDg) access:`llot`

### Test

Modify the contents of the file as follows.

1. `config.py` line 35 `mode="train"` change to `model="valid"`;
2. `config.py` line 79 `model_path=f"results/{exp_name}/g-last.pth"` change to `model_path=f"<YOUR-WEIGHTS-PATH>.pth"`;
3. Run `python validate.py`.



<p align="center">
<img src="assets/mnist.gif" width="300" height="300"><br>
</p>

### Train

Modify the contents of the file as follows.

1. `config.py` line 35 `mode="valid"` change to `model="train"`;
2. Run `python train.py`.

If you want to load weights that you've trained before, modify the contents of the file as follows.

1. `config.py` line 35 `mode="valid"` change to `model="train"`;
2. `config.py` line 51 `start_epoch=0` change to `start_epoch=XXX`;
3. `config.py` line 52 `resume=False` change to `resume=True`;
4. `config.py` line 53 `resume_d_weight=""` change to `resume_d_weight=<YOUR-RESUME-D-WIGHTS-PATH>`;
5. `config.py` line 54 `resume_g_weight=""` change to `resume_g_weight=<YOUR-RESUME-G-WIGHTS-PATH>`;
6. Run `python train.py`.
