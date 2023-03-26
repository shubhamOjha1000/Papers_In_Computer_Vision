#  Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning
- <ins>Author, Venue & Year</ins>: **Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi, AAAI, 2017**
### [Original Paper](https://arxiv.org/abs/1602.07261) || [**Paper Report**](https://github.com/AdiNarendra98/Papers-on-Vision/blob/main/Paper%20Summaries/16.Inception-v4%2C%20Inception-ResNet%20and%20the%20Impact%20of%20Residual%20Connections%20on%20Learning/Inception-v4%2C%20Inception-ResNet%20and%20the%20Impact%20of%20Residual%20Connections%20on%20Learning.pdf)

## Summary
  * Inception v4 is like Inception v3, but
    * Slimmed down, i.e. some parts were simplified
    * One new version with residual connections (Inception-ResNet-v2), one without (Inception-v4)
  * They didn't observe an improved error rate when using residual connections.
  * They did however oberserve that using residual connections decreased their training times.
  * They had to scale down the results of their residual modules (multiply them by a constant ~0.1). Otherwise their networks would die (only produce 0s).
  * Results on ILSVRC 2012 (val set, 144 crops/image):
    * Top-1 Error:
      * Inception-v4: 17.7%
      * Inception-ResNet-v2: 17.8%
    * Top-5 Error (ILSVRC 2012 val set, 144 crops/image):
      * Inception-v4: 3.8%
      * Inception-ResNet-v2: 3.7% 

* Architecture
  * Basic structure of Inception-ResNet-v2 (layers, dimensions):
    * `Image -> Stem -> 5x Module A -> Reduction-A -> 10x Module B -> Reduction B -> 5x Module C -> AveragePooling -> Droput 20% -> Linear, Softmax`
    * `299x299x3 -> 35x35x256 -> 35x35x256 -> 17x17x896 -> 17x17x896 -> 8x8x1792 -> 8x8x1792 -> 1792 -> 1792 -> 1000`
  * Modules A, B, C are very similar.
  * They contain 2 (B, C) or 3 (A) branches.
  * Each branch starts with a 1x1 convolution on the input.
  * All branches merge into one 1x1 convolution (which is then added to the original input, as usually in residual architectures).
  * Module A uses 3x3 convolutions, B 7x1 and 1x7, C 3x1 and 1x3.
  * The reduction modules also contain multiple branches. One has max pooling (3x3 stride 2), the other branches end in convolutions with stride 2.
