# Generative Models and VAEs

Reference for how generative models work, what makes them different from classifiers, and how autoencoders and variational autoencoders generate new data.

---

## Discriminative vs Generative

A discriminative model answers "which class is this?" It draws boundaries between categories. A generative model answers "what does a realistic sample look like?" It learns the distribution of the data well enough to draw new samples from it.

## Generation Is Sampling

A generative model learns the probability distribution of its training data: what is likely and what is not. To generate, it draws a random sample from that learned distribution. Each sample is new but looks like it belongs. The randomness is why you get variety instead of one fixed answer.

## The Generative Family

| Approach | How it generates |
| :--- | :--- |
| **Autoencoders / VAEs** | Encode to a latent code, then decode |
| **GANs** | A generator competes against a discriminator |
| **Diffusion** | Remove noise step by step |
| **Transformers / LLMs** | Predict the next token |

Different recipes, same goal: model a data distribution and sample from it.

## Autoencoders

An autoencoder has two parts:

- **Encoder:** compresses the input into a small latent code.
- **Decoder:** rebuilds the input from that code.

The bottleneck is the point. Because the code is small, the network cannot simply copy the input; it has to keep only what matters. Similar inputs end up near each other in latent space, which gives a useful compact representation.

A plain autoencoder reconstructs well but is not built for generation. Random points in its latent space often decode into nonsense because the space has gaps.

## Variational Autoencoders

A VAE fixes the gap problem so you can sample from it.

- The encoder outputs a distribution (a mean and a standard deviation) instead of a single point.
- A point is sampled from that distribution before decoding.
- Training keeps the latent space smooth and centered around the origin.

Because the latent space is smooth and organized, sampling a random point and decoding it produces a realistic new sample. You can also interpolate: walking between two points in latent space morphs one output smoothly into another.

### The Two Loss Terms

A VAE is trained with two terms working together:

1. **Reconstruction loss:** the decoded output should match the input.
2. **KL divergence:** the encoded distribution should stay close to a standard normal.

The reconstruction term keeps outputs faithful. The KL term keeps the latent space well-shaped so sampling works.

### The Reparameterization Trick

Sampling is random, and you cannot backpropagate through a random draw directly. The reparameterization trick rewrites the sample as `z = mean + std * epsilon`, where `epsilon` is drawn from a standard normal. Now the randomness sits in `epsilon`, and gradients flow through `mean` and `std` so the encoder can still learn.

## VAE at a Glance

- Encode input to a mean and spread.
- Sample a latent point.
- Decode it into a new sample.
- Train with reconstruction loss plus KL divergence.

This is the model you build in Lab 1.3 to generate new handwritten digits.
