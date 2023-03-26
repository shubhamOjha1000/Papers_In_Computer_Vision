#  Denoising Diffusion Probabilistic Models

- <ins>Author, Venue & Year</ins>: **Jonathan Ho, Ajay Jain, Pieter Abbeel, NeurIPS,2020**

### [Original Paper](https://arxiv.org/abs/2006.11239) 

## Summary

- This paper by Ho et al. from Pieter Abbeel’s lab at UC Berkeley presents high quality image samples using diffusion probabilistic models (also called diffusion models), a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.

- Their best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding.

- On the unconditional CIFAR10 dataset, they obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN.
