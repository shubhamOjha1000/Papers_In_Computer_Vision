# Very Deep Convolutional Networks for Large-Scale Image Recognition

- This repo is an attempt to implement the paper [**Very Deep Convolutional Networks for Large-Scale Image Recognition**](https://arxiv.org/abs/1409.1556)
in **Tensorflow**. 


## Dataset

- Link: [**ILSVRC2010**](http://www.image-net.org/challenges/LSVRC/2010/download-all-nonpub)
- Training size: *1261406 images*
- Validation size: *50000 images*
- Test size: *150000 images*


## How to Run

- To train: ``python model.py <path-to-training-data> --train true --test false``
- To test: ``python model.py <path-to-training-data> --train false --test true``

- screenlog-train.0: The log file after running ``python model.py <path-to-training-data> --train true`` in `screen <http://man7.org/linux/man-pages/man1/screen.1.html>`_
- model and logs: `google drive <https://drive.google.com/open?id=1FIXAjopwMHYfXB4_EEDVhxnd0gysoMpI>`_

## Preprocessing

The following preprocessing steps are performed

1. **Rescaling**: Isotropically rescale the image such that the smallest size is randomly drawn from ``[256, 512]``. In short *isotropically* means the ratio of width to height of the original image should match with that of the new image.
2. **Cropping**: Randomly crop the image from the rescaled image to get a size of ``(224, 224)``.
3. **Augmentation**: Augment the data in two ways
     i. Horizontally flip the image with 50 % probability
     ii. Add PCA as calculated by `AlexNet <https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf>`_ to the processed image to give color shifting.
4. **Subtract mean**: Finally subtract the mean activity from the processed image.

**Note**: To calculate eigenvalues and eigenvectors for the imagenet dataset will require significant amount of RAM. So the values are taken from `stackoverflow <https://stackoverflow.com/questions/43328600/does-anyone-have-the-eigenvalue-and-eigenvectors-for-alexnets-pca-noise-from-th>`_ and hardcoded while adding PCA.

## Tensorflow Generated Graphs

**top1 accuracy**:

.. image:: pictures/top1.png

**top5 accuracy**:

.. image:: pictures/top5.png

**loss**:

.. image:: pictures/loss.png

## Accuracies


 * Top1 accuracy: **67.1013%**
 * Top5 accuracy: **85.1460%**
