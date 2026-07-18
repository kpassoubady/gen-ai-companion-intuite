# Lab 1.2 - Image Classification with PyTorch

**Day 1 - Session 2**

## Objectives

1. Load a small slice of the FashionMNIST image dataset.
2. Build a neural network with PyTorch.
3. Train it with a standard training loop.
4. Evaluate accuracy on a held-out test set.

## Setup

Run in Google Colab (recommended): open `start/lab1_2_image_clf.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

To run locally instead, activate the repo virtual environment and install
requirements. See the [root README](../../README.md).

## Instructions

1. Open `start/lab1_2_image_clf.ipynb`.
2. Fill in each `# TODO`: build the model, write the five training steps, and
   compute test accuracy.
3. Run every cell. Training loss should drop each epoch and test accuracy should
   land around 0.82-0.86 on this small slice.
4. Try the stretch goals (a deeper network or a convolutional network).

The dataset and epochs are capped so every cell finishes in a couple of minutes
on a Colab CPU runtime. No GPU needed.

## Getting Stuck?

The full working code is in `solution/lab1_2_image_clf.ipynb`.
