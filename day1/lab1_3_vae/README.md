# Lab 1.3 - Generate Handwritten Digits with a VAE

**Day 1 - Session 3**

## Objectives

1. Build a small variational autoencoder (VAE) in PyTorch.
2. Implement the reparameterization trick and the VAE loss.
3. Train the VAE on MNIST digits.
4. Sample the latent space to generate brand-new digits.

## Setup

Run in Google Colab (recommended): open `start/lab1_3_vae.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

To run locally instead, activate the repo virtual environment and install
requirements. See the [root README](../../README.md).

## Instructions

1. Open `start/lab1_3_vae.ipynb`.
2. Fill in each `# TODO`: the reparameterization trick, the VAE loss, the
   training steps, and the sampling code.
3. Run every cell. The average loss should drop each epoch, and the final grid
   should show recognizable (if slightly blurry) generated digits.
4. Try the stretch goals: interpolate between two latent points, or visualize a
   2D latent space.

The dataset and epochs are capped so every cell finishes in a few minutes on a
Colab CPU runtime. No GPU needed.

## Getting Stuck?

The full working code is in `solution/lab1_3_vae.ipynb`.
