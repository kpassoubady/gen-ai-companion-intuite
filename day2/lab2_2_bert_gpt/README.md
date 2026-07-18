# Lab 2.2 - Introduction to BERT and GPT

**Day 2 - Session 2**

## Objectives

1. Use BERT (an encoder) to fill in a masked word with both-direction context.
2. Use GPT-2 (a decoder) to continue a prompt left to right.
3. Inspect tokens and next-token probabilities to see how generation works.

## Setup

Run in Google Colab (recommended): open `start/lab2_2_bert_gpt.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

To run locally instead, activate the repo virtual environment and install
requirements. See the [root README](../../README.md).

This lab uses small Hugging Face models (`distilbert-base-uncased` and `gpt2`).
No API key and no GPU needed. Models download once, then cache.

## Instructions

1. Open `start/lab2_2_bert_gpt.ipynb`.
2. Fill in each `# TODO`: build the fill-mask pipeline, tokenize text, generate
   with GPT-2, and turn logits into next-token probabilities.
3. Run every cell. BERT should fill "Paris is the capital of [MASK]." with
   "france", and GPT-2 should continue the prompt with a plausible sentence.
4. Try the stretch goals: switch greedy decoding to sampling, or write your own
   masked sentence.

## Getting Stuck?

The full working code is in `solution/lab2_2_bert_gpt.ipynb`.
