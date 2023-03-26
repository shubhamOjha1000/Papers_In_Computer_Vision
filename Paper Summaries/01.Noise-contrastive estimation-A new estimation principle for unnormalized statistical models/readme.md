# Noise-contrastive estimation-A new estimation principle for Unnormalized Statistical Models


### [Original Paper](https://proceedings.mlr.press/v9/gutmann10a/gutmann10a.pdf) || [Annotated Paper](https://github.com/AdiNarendra98/Papers-on-Vision/blob/main/Paper%20Summaries/01.Noise-contrastive%20estimation-A%20new%20estimation%20principle%20for%20unnormalized%20statistical%20models/Annotated%20Paper%201.pdf)

- <ins>Authors,Venue & Year</ins>: **Michael Gutmann,Aapo Hyvarinen,AISTATS, 2010**

## Summary

* This paper by Gutmann and Hyvarinen in AISTATS 2010 introduced the **concept of negative sampling that forms the basis of contrastive learning**.

* They propose a **new estimation principle for parameterized statistical models, noise-contrastive estimation, which discriminates between observed data and artificially generated noise**. This is accomplished by **performing nonlinear logistic regression to discriminate between the observed data and some artificially generated noise, using the model log-density function in the regression nonlinearity**. They show that this **leads to a consistent (convergent) estimator of the parameters**, and also **analyze the asymptotic variance**.

* In particular, the method is shown to **directly work for unnormalized models, i.e. models where the density function does not integrate to one**. The **normalization constant can be estimated just like any other parameter**.

* For a tractable **ICA model**, they compare the method with other estimation methods that can be used to learn **unnormalized models, including score matching, contrastive divergence, and maximum-likelihood where the normalization constant is estimated with importance sampling**.

* Simulations show that **noise-contrastive estimation offers the best trade-off between computational and statistical efficiency**.

* They apply the method to the modeling of natural images and show that **the method can successfully estimate a large-scale two-layer model and a Markov random field**.

* They use a **VERY simple problem to compare the performance of NCE to MLE with importance sampling, contrastive divergence (CD) and score-matching** (and MLE, which gives the reference performance. MLE requires an **analytical expression for the normalizing constant**). CD has the best performance, but **NCE is apparently more computationally efficient**. I do not think such a simple problem say too much though.
