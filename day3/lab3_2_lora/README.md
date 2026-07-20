# Lab 3.2 - Fine-Tune a Small Language Model with LoRA

**Day 3 - Session 2**

## Objectives

1. Wrap a small instruction model with a LoRA adapter using `peft`.
2. Train only the adapter (a fraction of a percent of the weights) on a tiny
   styled dataset.
3. Compare generations before and after to see the style transfer.

## Setup

Run in Google Colab (recommended): open `start/lab3_2_lora.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

This lab runs offline with a local model and needs no API key or GPU; it
finishes on a Colab CPU or T4 runtime in a few minutes.

The default model `Qwen/Qwen2.5-0.5B-Instruct` is about 950 MB and downloads
once per machine. On weak classroom wifi, switch to the smaller fallback
`HuggingFaceTB/SmolLM2-360M-Instruct` (about 690 MB) in the model cell.

## Instructions

1. Open `start/lab3_2_lora.ipynb`.
2. Fill in each `# TODO`: build the `LoraConfig` and wrap the model, then write
   the forward, backward, and optimizer step inside the training loop.
3. Run every cell. Before training the answers are plain; after four short
   epochs the two held-out prompts come back in the pirate style, and the loss
   falls each epoch.
4. Try the stretch goals: save and measure the tiny adapter, swap in the
   SmolLM2 fallback, or train your own style.

## Getting Stuck?

The full working code is in `solution/lab3_2_lora.ipynb`, with the expected
behavior described in the final markdown cell. QLoRA and 4-bit quantization
stay a concept in this course because they need a CUDA GPU; this lab uses
standard LoRA on CPU.
