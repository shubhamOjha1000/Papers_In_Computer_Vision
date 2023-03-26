# AlexNet- Image Classification with Deep Convolution Neural Networks

- This repository contains implementation of [**AlexNet Paper**](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
(ImageNet Classification with Deep Convolutional Neural Networks) using **Tensorflow** 
- The network tested with the
[**CIFAR-10 dataset**](https://www.cs.toronto.edu/~kriz/cifar.html).
<p align="center">
<img src="https://github.com/AdiNarendra98/Papers-on-Vision/blob/main/Re-Implementations/02.ImageNet%20Classification%20with%20Deep%20Convolutional%20Neural%20Networks%20/AlexNet(Tensorflow)/alexnet.png"><br>
</p>


##  Dependencies
* Python 3
* numpy
* scipy
* pillow
* tensorflow

## Dataset: CIFAR-10 dataset
Before train and evaluate the network, you should download the following dataset:

* CIFAR-10 Dataset: https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

Extract the `cifar-10-python.tar.gz` file, then your folder structure should be like the following image:

![Folder Structure](folder_structure.png)

## Training CIFAR-10 dataset
To train the network with cifar-10 dataset, type the following command at the command prompt:
```
python3 ./train.py
```

Sample images from cifar-10 dataset:

![cifar_10_sample](cifar_10_sample.jpg)

## Results

### Epoch 0
```
Train Accuracy = 0.100
Test Accuracy = 0.100
```

### Epoch 1
```
Train Accuracy = 0.305
Test Accuracy = 0.303
```

### Epoch 2
```
Train Accuracy = 0.408
Test Accuracy = 0.402
```

...

### Epoch 50
```
Train Accuracy = 0.986
Test Accuracy = 0.721
```

...

### Epoch 100
```
Final Train Accuracy = 1.000
Final Test Accuracy = 0.739
```

# Evaluating CIFAR-10 dataset
To evaluate the network with cifar-10 dataset, type the following command at the command prompt:
```
python3 ./evaluate.py
```

