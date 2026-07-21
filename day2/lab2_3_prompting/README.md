# Lab 2.3 - Prompting Techniques and Generative Tasks

**Day 2 - Session 3**

> **Requires an API key.** This lab calls a hosted LLM through the shared client.
> No key? Use the no-key version at [`../lab2_3_prompting_nokey/`](../lab2_3_prompting_nokey/),
> which teaches the same techniques on a small local model.

## Objectives

1. Summarize text with zero-shot prompting, then refine with a role and format.
2. Generate a Python function from a clear specification.
3. Label support tickets with zero-shot, then improve with few-shot examples.

## Setup

Run in Google Colab (recommended): open `start/lab2_3_prompting.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

This lab calls an LLM API through the shared client (`get_completion`). Provide a
key one of these ways:

- **Colab:** add `OPENAI_API_KEY` as a Colab secret, or type it when prompted.
- **Local:** copy `.env.example` to `.env` and set your provider and key. See the
  [root README](../../README.md).

All calls use the `mini` tier to keep cost low. Runs on CPU; no GPU needed.

## Instructions

1. Open `start/lab2_3_prompting.ipynb`.
2. Fill in each `# TODO`: zero-shot and refined summaries, code generation, and
   zero-shot plus few-shot labeling.
3. Run every cell. The refined summary should be tighter than the zero-shot one,
   the generated function should have type hints and a docstring, and the three
   tickets should label as BILLING, BUG, and HOWTO.
4. Try the stretch goals: add chain-of-thought, or ask for JSON labels and parse
   them.

## Getting Stuck?

The full working code is in `solution/lab2_3_prompting.ipynb`.
