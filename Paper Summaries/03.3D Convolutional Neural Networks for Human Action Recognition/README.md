# 3D Convolutional Neural Networks for Human Action Recognition
- <ins>Authors,Venue & Year</ins>: **Shuiwang Ji,Wei Xu ,Ming Yang ,Kai Yu at IEEE PAMI ,2012**

### [Original Paper](https://www.dbs.ifi.lmu.de/~yu_k/icml2010_3dcnn.pdf)

## Summary
- This paper by Ji et al. from Arizona State University in IEEE PAMI 2012 **introduced 3D CNNs**.

- The author maintains that **3D convolution neural network extracts more contiguous information, such as spatial information, but not losing during the process than the 2D ones**.

- **3D convolution means that the kernel matrix is M x H x W**. It will **operate along the contiguous feature maps, such as 3 maps**. Hence, the **kernel matrix is Rx M x H x W**. { R = number of contiguous maps(R = (M-3(temporal dimension))/1+1), M = previous channel, H = kernel height, W = kernel width }
