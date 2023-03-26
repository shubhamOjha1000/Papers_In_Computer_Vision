# Generative Adversarial Networks
- <ins>Author, Venue & Year</ins>: **,Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio, NeurIPS 2014**

### [Original Paper](https://arxiv.org/abs/1406.2661)

## Summary

### Overview
- The paper proposes an **adversarial approach for estimating generative models where one model (generative model) tries to learn a data distribution and another model (discriminative model) tries to distinguish between samples** from the generative model and original data distribution.

### Adversarial Net
- Two models - **Generative Model(G) and Discriminative Model(D)**
- Both are multi-layer perceptrons.
- *G* takes as **input a noise variable z and outputs data sample x(=G(z))**.
- *D* takes as **input a data sample x and predicts whether it came from true data or from G**.
- *G* tries to **minimise log(1-D(G(z)))** while *D* tries to **maximise the probability of correct classification**.
- Think of it as a **minimax game between 2 player**s and the **global optimum would be when *G* generates perfect samples and *D* can not distinguish between the samples** (thereby always returning 0.5 as the probability of sample coming from true data).
- Alternate between **k steps of training *D* and 1 step of training *G* so that *D* is maintained near its optimal solution**.
- When starting training, the **loss log(1-D(G(z))) would saturate as *G* would be weak. Instead maximise log(D(G(z)))**
- The paper contains the **theoretical proof for global optimum of the minimax game**.
- There is **no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples**.

### Strengths

- **Computational Advantages**
  * Backprop is sufficient for training with no need for Markov chains or performing inference
  * A variety of functions can be used in the model.
- Since *G* is trained only using the gradients from *D*, fewer chances of directly copying features from the true data.
- Can represent **sharp (even degenerate) distributions**.

### Weakness

- *D* must be well synchronised with *G*.
- While *G* may learn to sample data points that are indistinguishable from true data, no explicit representation can be obtained.

## Resources
- #### Found this presentation on GANs to be helpful,Check it out here 👉🏻: [**GANS Presentation**](https://github.com/AdiNarendra98/Papers-on-Vision/blob/main/Paper%20Summaries/05.Generative%20Adversarial%20Networks%20/GANs%20Presentation.pdf)
