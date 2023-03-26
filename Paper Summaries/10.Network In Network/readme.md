#  Network in Network
- <ins>Author, Venue & Year</ins>: **Min Lin, Qiang Chen, Shuicheng Yan, ICLR, 2014**
### [Original Paper](https://arxiv.org/abs/1312.4400) || [**Paper Report**](https://github.com/AdiNarendra98/Papers-on-Vision/blob/main/Paper%20Summaries/10.Network%20In%20Network/Network%20in%20Network.pdf)

## Summary

- This paper studies a very natural generalization of convolutional layers
by replacing a single filter that slides over the input feature map with
a "micro network" (multi-layer perceptron). The authors argue that good
abstractions are highly non-linear functions of input data and instead of
generating an overcomplete number of feature maps and shrinking them down
in higher layers (as is the case in traditional CNNs), it would be beneficial
to generate better representations on each local patch, before feeding into
the next layer. Main contributions:

- Replaces the convolutional filter with a multi-layer perceptron.
- Instead of fully connected layers, uses global average pooling.

## Strengths

- Natural generalization of convolutional layers and thorough analysis.
- Global average pooling of feature layers is easier to interpret and less prone to overfitting.
- Better or at par with state-of-the-art classification results on CIFAR-10, CIFAR-100, SVHN, MNIST.

## Weaknesses / Notes

- Should have explored NIN without dropout.
- Results on ImageNet missing.
- The global average pooling idea, although interpretable,
doesn't seem to give easily to fine-tuning the network to
other datasets. In finetuning, we usually replace and learn
just the last layer.
