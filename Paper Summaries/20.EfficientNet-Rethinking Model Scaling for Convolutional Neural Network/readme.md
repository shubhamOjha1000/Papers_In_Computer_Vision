#  EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks

- <ins>Author, Venue & Year</ins>: **Mingxing Tan, Quoc V. Le, ICML,2019**

### [Original Paper](https://arxiv.org/pdf/1905.11946v5.pdf) 

## Summary

- The paper EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks introduces a new principle method to scale up ConvNets.
- To get a better accuracy, CNN needs to have a careful balance between depth width and resolution. However, process of scaling up ConvNets has never been understood.
- Most common way was to scale up ConvNets by their depth or width.
- Another less common way was to scale up models by image resolution. So far, we only scale one dimension at the time.
   * Depth: Deeper ConvNets capture more complex features and generalize well. However, more difficult to train due to vanishing gradient. Although techniques such as “skip connections” and “batch normalization” are alleviating the training problem, the accuracy gain diminishes for very deep network.

   * Width: Wider networks tend to capture more fined-grained features and are easierto train. However, accuracy for such network tends to quickly saturate.

   * Resolution: With higher resolution input images, ConvNets can potentially capture more fine-grained patterns. However, for very high resolutions, the accuracy gains disminishes.

We can then think about scaling multiple dimension at one time. It is possible to scale two or three dimensions arbitrarily, requiring manual tuning which often yields to sub-optimal accuracy and efficiency.

- In this paper, they are trying to address the following issue:
“**Is there a principled method to scale up ConvNets that can achieve better accuracy and efficiency ?**”

- Their empirical study shows that it is critical to balance all dimensions of network (width/depth/resolution) at the same time.

- Such balance can be achieved by scaling each of them by a constant ratio.

- This method is called “**compound scaling method**”, which consists of **uniformly scales the network width, depth and resolution with a set of fixed scaling coefficients**.

- The intuition comes from the following fact:
  * If the input image is bigger (resolution), then there is more complex-features and fine-grained patterns. To capture more complex-feature, the network needs bigger receptive field which is achieved by adding more layers (depth). To capture more fine-grained patterns, the network needs more channels.
  
  

