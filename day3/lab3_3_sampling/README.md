# Lab 3.3 - Customize Output with Sampling Parameters

**Day 3 - Session 2**

## Objectives

1. Generate text with a small GPT-2 style model using Hugging Face `generate()`.
2. Compare greedy, temperature, top-k, top-p, and beam search decoding.
3. See which strategies are deterministic and which you tune for variety.

## Setup

Run in Google Colab (recommended): open `start/lab3_3_sampling.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

This lab runs fully offline with a small local model (`distilgpt2`). No API key
and no GPU needed; it finishes on a Colab CPU runtime in a couple of minutes.

## Instructions

1. Open `start/lab3_3_sampling.ipynb`.
2. Fill in each `# TODO`: the greedy call, the temperature, top-k, and top-p
   helper functions, and the beam search call.
3. Run every cell. Greedy and beam search print the same text each run;
   temperature, top-k, and top-p change with the settings.
4. Try the stretch goals: fix a seed for repeatable sampling, combine
   temperature with top-p, and inspect multiple beams.

## Getting Stuck?

The full working code is in `solution/lab3_3_sampling.ipynb`, with the expected
behavior described in the final markdown cell.
