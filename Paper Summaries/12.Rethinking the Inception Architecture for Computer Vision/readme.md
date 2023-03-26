#  Rethinking the Inception Architecture for Computer Vision
- <ins>Author, Venue & Year</ins>: **Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, Zbigniew Wojna,CVPR,2016**
### [Original Paper](https://arxiv.org/abs/1512.00567) || [**Paper Report**](https://github.com/AdiNarendra98/Papers-on-Vision/blob/main/Paper%20Summaries/12.Rethinking%20the%20Inception%20Architecture%20for%20Computer%20Vision/Rethinking%20the%20Inception%20Architecture%20for%20Computer%20Vision.pdf)

## Summary
* This paper by Szegedy et al. from Google in CVPR 2016 proposed InceptionV2, V3 by improving the Inception model based on the following principles:
   - Using the same principle as VGG, the authors factorized 5×5 and 7×7 (in InceptionV3) convolutions to two and three 3×3 sequential convolutions respectively.This improves computational speed and utilizes far less parameters.

  - Used spatially separable convolutions. Simply, a **3×3kernel is decomposed into two smaller ones: a 1×3 and a 3×1 kernel, which are applied sequentially**.

  - Widened the inception modules (more number of filters).

  - Distributed the computational budget in a balanced way between the depth and width of the network.

  - Added **batch normalization**.
