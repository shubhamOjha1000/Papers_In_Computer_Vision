#  An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

- <ins>Author, Venue & Year</ins>: **Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby,ICLR,2021**

### [Original Paper](https://arxiv.org/abs/2010.11929) 

## Summary

- In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place.

- This paper by Dosovitskiy et al. from Google Brain in ICLR 2021 shows that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks.

- Inspired by the Transformer scaling successes in NLP, we experiment with applying a standard Transformer directly to images, with the fewest possible modifications. To do so, they split an image into patches and provide the sequence of linear embeddings of these patches as an input to a Transformer. Image patches are treated the same way as tokens (words) in an NLP application. They train the model on image classification in supervised fashion.

- They introduce three ViT configurations (Base, Large, and Huge) in the form of two models: ViT-H/14 and ViT-L/16 (where the notation used is ViT-C/N, C is used to indicate the model size and N is the input patch size; for instance, ViT-L/16 means the “Large” variant with 16×16 input patch size).

- When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), the proposed Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.

### Notes:
- Found this [Presentation](https://tugot17.github.io/Vision-Transformer-Presentation/#/2) to be helpful in understanding the paper.
