# Rethinking the Inception Architecture for Computer Vision

- This is the implementation of [**Rethinking the Inception Architecture for Computer Vision**](https://arxiv.org/abs/1512.00567) using **Tensorflow**.
- The dataset used for evaluation is [**CIFAR-10**](https://www.cs.toronto.edu/~kriz/cifar.html)

## How to run
    python main.py -p ./ -g 0 


## Working

### Data Augmentation  
  - Train: 
    - Pictures are randomly **resized in the range of [256, 512], then 224x224 patches are extracted randomly and are normalized locally**. 
    - Horizontal **flipping is applied with 0.5 probability**.  
  - Test: 
    - Pictures are **resized to 384x384**, then they are normalized locally. Single image test is used to calculate total accuracy. 

### Auxiliary Classifiers 
  - No implementation  

### Gradient clipping  
  - **2.0**  

### SGD momentum
  - **lr=0.1, momentum=0.9**


### Learning rate  
  - Initial learning rate is **0.1** acoording to the paper, and it is **multiplied by 0.94 at every 2 epochs**.

### Weight decay  
  - Weight decay is **4.0*10^-5**.


## Results

| **Network**              | **depth**  | **total accuracy (%)** |
|:---------------------|--------|-------------------:|
| **This implementation**   | 49     | **94.74**              |

<p align="center">
<img src="https://github.com/nutszebra/googlenet_v3/blob/master/loss.jpg" alt="loss" title="loss">
<img src="https://github.com/nutszebra/googlenet_v3/blob/master/accuracy.jpg" alt="total accuracy" title="total accuracy">
</p>
