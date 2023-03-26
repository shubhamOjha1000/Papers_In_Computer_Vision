# Going Deeper with Convolutions
- <ins>Author, Venue & Year</ins>: **Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, Andrew Rabinovich, CVPR, 2014**

### [Original Paper](https://arxiv.org/abs/1409.4842) || [**Paper Report**](https://github.com/AdiNarendra98/Papers-on-Vision/blob/main/Paper%20Summaries/07.Going%20Deeper%20with%20Convolutions/Going%20deeper%20with%20convolutions.pdf)

## Summary

- This paper introduces a neural network architecture
that is deeper and wider, yet optimizing for computational
efficiency by approximating the expected sparse structure
(following from Arora et al's work) using readily available
dense blocks. An ensemble of 7 models (all with the same
architecture but different image sampling) achieved top spot
in the classification task at ILSVRC2014.

- "Their main result states that if the probability distribution of the data-set is representable by a large, very sparse deep neural network, then the optimal network topology can be constructed layer by layer by analyzing the correlation statistics of the activations of the last layer and clustering neurons with highly correlated outputs."

## Main contributions:

- A more generalized exploration of the NIN architecture,
called the Inception module.
    - 1x1 convolutions to capture dense information clusters
    - 3x3 and 5x5 to capture more spatially spread out
    clusters
    - Ratio of 3x3 and 5x5 to 1x1 convolutions increases as we go deeper
    as features of higher abstraction are less spatially
    concentrated.
- To avoid the blow-up of output channels cause by merging outputs
of convolutional layers and pooling layer, they use 1x1 convolutions
for dimensionality reduction. This has the added benefit of another
layer of non-linearity (and thus increasing discriminative capability).
- Multiple intermediate layers are tied to the objective function. Since
features produced by intermediate layers of a deep network are
supposed to be very discriminative, and to strengthen the gradient signal
passing through them during back-propagation, they attach auxiliary classifiers
to intermediate layers.
    - During training, they do a weighted sum of this loss with the total loss
    of the network.
    - At test time, these auxiliary networks are discarded.
    - Architecture: average pooling, 1x1 convolution (for dimensionality reduction),
    dropout, linear layer with softmax.
    
## Strengths

- Achieved state of the art results for classification and detection in the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC) 2014.

## Weaknesses / Notes

- Even though the authors try to explain some of the intuition, most of the design decisions seem arbitrary.
the design decisions seem arbitrary.
