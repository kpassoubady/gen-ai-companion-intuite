# Lab 2.3 (No Key) - Prompting Techniques on a Local Model

**Day 2 - Session 3**

This is the no-key version of [Lab 2.3](../lab2_3_prompting/). Use it if you do
not have an LLM API key. It teaches the same prompting techniques.

## How this runs without an API key

This lab uses `google/flan-t5-base`, a small instruction-tuned model that
downloads once (about 1 GB) and runs on your machine (CPU is fine). There is no
provider key and no shared client. The prompting techniques are identical to the
API lab; only the call site changes (`generate(...)` instead of
`get_completion(...)`). A small local model is weaker than a hosted one, so the
tasks here are ones it handles well: labeling, summarization, and step-by-step
reasoning.

## Objectives

1. Label support tickets with zero-shot prompting, then improve with few-shot.
2. Summarize text zero-shot, then refine with a role and format.
3. Use chain-of-thought to turn a wrong direct answer into a correct one.

## Setup

Run in Google Colab (recommended): open `start/lab2_3_prompting_nokey.ipynb`
with the "Open in Colab" badge and run the first cell to install `transformers`
and `torch`. No API key and no `.env` needed. Runs on CPU; no GPU required.

## Instructions

1. Open `start/lab2_3_prompting_nokey.ipynb`.
2. Fill in each `# TODO`: zero-shot and few-shot labeling, zero-shot and refined
   summaries, and the direct vs step-by-step reasoning calls.
3. Run every cell. The tickets should label as BILLING, BUG, and HOWTO, the
   summaries should be short and on topic, and the step-by-step answer to the
   weeks question should reach 21.
4. Try the stretch goals: translation, output validation, and noting where a
   hosted model would do better.

## Getting Stuck?

The full working code is in `solution/lab2_3_prompting_nokey.ipynb`.
