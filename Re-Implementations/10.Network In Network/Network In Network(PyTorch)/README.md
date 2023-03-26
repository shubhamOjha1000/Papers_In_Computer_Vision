# Network in Network
- This is a PyTorch implementation of [**Network In Network**](https://arxiv.org/abs/1312.4400)  
- The dataset used is [**Cifar10**](https://www.cs.toronto.edu/~kriz/cifar.html). 
- All settings are base on the [**network-in-network**](https://gist.github.com/mavenlin/e56253735ef32c3c296d) model in **Caffe model zoo**.

## Instructions
```bash
$ git clone https://github.com/AdiNarendra/Papers-on-Vision/Re-Implementations/10.Network in Network/Network in Network(PyTorch)
$ cd Network in Network(PyTorch)
$ mkdir data
```
Then download the data from [this link](https://drive.google.com/open?id=0B-7I62GOSnZ8Z0ZCVXFtVnFEaTg) and uncompress it into the ```./data/``` directory. Now you can train the model by running
```bash
$ python original.py
```

## Accuracy
By tweaking hyper-parameters, the model can reach the **accuracy of 89.64%**, which is better than other available Torch/PyTorch implementations.

