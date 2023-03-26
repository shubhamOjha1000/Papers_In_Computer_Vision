# AlexNet-ImageNet Classification with Deep Convolutional Neural Networks
- <ins>Authors,Venue & Year</ins>: **Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton, NIPS, 2012**
### [Original Paper](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) || [Paper Report](https://github.com/AdiNarendra98/Papers-on-Vision/blob/main/Paper%20Summaries/02.ImageNet%20Classification%20with%20Deep%20Convolutional%20Neural%20Networks%20/ImageNet%20Classification%20with%20Deep%20Convolutional%20Neural%20Networks.pdf)
## Summary

### Overview
This paper introduces a deep convolutional neural network (CNN) architecture that achieved record-breaking performance in the 2012 ImageNet LSVRC. Notably, it brings together a bunch of neat ideas in an end-to-end, trainable model. Main contributions:
- Achieves state-of-the-art performance in ILSVRC-2012.
- Makes available an efficient, parallelized GPU implementation of their model.
- Describes in detail the features of their model that help in improving performance and reducing training time, along with extensive ablative studies.
- Uses data augmentation and dropout to prevent overfitting.
 #### Architecture
- The networks comes with:

  * 5 conv layers with maxpooling and ReLU;
  * 2 FC layers + softmax of 1000 classes;
  * Multi-GPU
  * Local response normalization (“This sort of response normalization implements a form of lateral inhibition inspired by the type found in real neurons, creating competition for big activities amongst neuron outputs computed using different kernels.”)
  * Overlapping pooling
  * Data augmentation
  * Dropout

### Strengths

- Uses (and popularizes) ReLUs instead of tanh as the non-linear activation unit, which makes training six times faster.
- Uses local response normalization and overlapped pooling.
- Data augmentation
  * Extracts random crops and performs image translations, horizontal reflections maintaining the label distribution.
  * Alters RGB pixel values by performing PCA on training set, and adding multiples of eigenvalues times a random variable drawn from a Gaussian to image. Provides invariance to changes in intensity and color of illumination.
- Dropout prevents overfitting. Randomly drops half of the neurons in the fully connected layers, and can be interpreted as averaging over exponentially-many dropout networks.

### Weaknesses / Notes

- Lacks theoretical insight. Design decisions are motivated solely by results.
