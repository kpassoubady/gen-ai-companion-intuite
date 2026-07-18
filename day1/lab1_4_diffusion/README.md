# Lab 1.4 - Generate Images with a Diffusion Pipeline

**Day 1 - Session 4**

## Objectives

1. Load a pre-trained diffusion pipeline from Hugging Face (inference only).
2. Generate images by denoising from random noise.
3. See how the number of denoising steps affects quality.
4. Use seeds to make results reproducible.

## Setup

Run in Google Colab (recommended): open `start/lab1_4_diffusion.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

To run locally instead, activate the repo virtual environment and install
requirements. See the [root README](../../README.md).

## Instructions

1. Open `start/lab1_4_diffusion.ipynb`.
2. Fill in each `# TODO`: call the pipeline, sweep the step count, and vary the
   seed.
3. Run every cell. You will see small 32x32 images that get smoother as the step
   count rises, and identical images repeat for a fixed seed.
4. Try the stretch goal: text-to-image with Stable Diffusion (a free T4 runtime
   is recommended, since it is much faster than CPU for the larger model).

The core lab uses a small unconditional model that generates in well under a
second on a Colab CPU runtime. No GPU needed for the core.

## Getting Stuck?

The full working code is in `solution/lab1_4_diffusion.ipynb`.
