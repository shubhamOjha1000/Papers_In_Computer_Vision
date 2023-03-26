# Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks
- <ins>Author, Venue & Year</ins>: **Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun,Arxiv,2016**

### [Original Paper]( https://arxiv.org/abs/1506.01497) || [**Paper Report**](https://github.com/AdiNarendra98/Papers-on-Vision/blob/main/Paper%20Summaries/14.Faster%20R-CNN-Towards%20Real-Time%20Object%20Detection%20with%20Region%20Proposal%20Networks/Faster%20R-CNN.pdf)

## Summary

* State-of-the-art object detection networks depend on region proposal algorithms to hypothesize object locations. Advances like SPPnet and Fast R-CNN have reduced the running time of these detection networks, exposing region proposal computation as a bottleneck.

* This paper by Ren et al. from University of Science and Technology of China and Microsoft Research in 2016 proposes a Region Proposal Network (RPN) for efficient and accurate region proposal generation that shares full-image convolutional features with the detection network, thus enabling nearly cost-free region proposals. By sharing convolutional features with the down-stream detection network, the region proposal step is nearly cost-free.

* An RPN is a fully convolutional network that simultaneously predicts object bounds and objectness scores at each position. The RPN is trained end-to-end to generate high-quality region proposals, which are used by Fast R-CNN for detection.

* They further merge RPN and Fast R-CNN into a single network by sharing their convolutional features – using the recently popular terminology of neural networks with ‘attention’ mechanisms, the RPN component tells the unified network where to look.

* For the very deep VGG-16 model, our detection system has a frame rate of 5fps (including all steps) on a GPU, while achieving state-of-the-art object detection accuracy on PASCAL VOC 2007, 2012, and MS COCO datasets with only 300 proposals per image. In ILSVRC and COCO 2015 competitions, Faster R-CNN and RPN are the foundations of the 1st-place winning entries in several tracks.

* Faster R-CNN enables a unified, deep-learning-based object detection system to run at near real-time frame rates. The learned RPN also improves region proposal quality and thus the overall object detection accuracy.
