# Lab 3.1 - Fine-Tune BERT for Sentiment

**Day 3 - Session 1**

## Objectives

1. Add a classification head to a pre-trained DistilBERT encoder.
2. Fine-tune it on a tiny labeled dataset with the Hugging Face `Trainer`.
3. Compare predictions before and after training to see fine-tuning work.

## Setup

Run in Google Colab (recommended): open `start/lab3_1_bert_finetune.ipynb` with
the "Open in Colab" badge and run the first cell to install dependencies.

This lab runs fully offline with a small local model
(`distilbert-base-uncased`). No API key and no GPU needed; it finishes on a
Colab CPU runtime in a few minutes.

## Instructions

1. Open `start/lab3_1_bert_finetune.ipynb`.
2. Fill in each `# TODO`: load the model with a 2-class head, complete the
   `predict` function, tokenize the dataset, and build and run the `Trainer`.
3. Run every cell. Before training the two test sentences are labeled near
   random; after 10 short epochs they come back correct with high confidence,
   and eval accuracy reaches 1.0 on the tiny eval set.
4. Read the summarization concept section, then try the stretch goals: an
   inference-only summarizer, more training data, or freezing the encoder.

## Getting Stuck?

The full working code is in `solution/lab3_1_bert_finetune.ipynb`, with the
expected behavior described in the final markdown cell. Summarization stays a
concept here so the hands-on time stays on one clean fine-tune.
