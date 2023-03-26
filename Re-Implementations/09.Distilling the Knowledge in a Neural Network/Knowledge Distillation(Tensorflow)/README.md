# Distilling-the-knowledge-in-neural-network
- This is an implementation of the paper [**Distilling the Knowledge in a Neural Network**](https://arxiv.org/abs/1503.02531) using **Tensorflow**.

## Working
- Running ``distill.py`` first trains a CNN network till 20k steps and then uses the prediction of this network as soft targets for a student network comprising of a single hidden fc layer.

- The student network trained using this way achieves a **test accuracy of 96.55%**.

- The student network when trained directly after running ``student.py`` without any knowledge from the teacher network achieves an **accuracy of only 94.08%**. 

- Thus using the **knowledge from another network we see an improvement in test accuracy of around 2.5%** .
