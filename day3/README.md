# Day 3 Labs - Fine-Tuning, RAG & Deployment

Hands-on labs for Day 3. Each lab has a `start/` notebook with `# TODO` markers
and a `solution/` notebook with the full working code. Every lab runs on a Google
Colab CPU or T4 runtime with no GPU required.

| Lab | Topic | Session |
| :--- | :--- | :--- |
| [Lab 3.1](lab3_1_bert_finetune/) | Fine-tune BERT for sentiment | Session 1 |
| [Lab 3.2](lab3_2_lora/) | Fine-tune a small language model with LoRA | Session 2 |
| [Lab 3.3](lab3_3_sampling/) | Customize output with sampling parameters | Session 2 |
| [Lab 3.4](lab3_4_rag/) | Build an end-to-end RAG pipeline | Session 3 |

The Day 3 capstone (a Small Business Finance Assistant) lives in
[`../capstone/`](../capstone/). No API key? Use the no-key version at
[`../capstone_nokey/`](../capstone_nokey/), which builds the same assistant on a
small local model.

## How to run

Open a lab's `start/` notebook with its "Open in Colab" badge and run the first
cell to install that lab's dependencies. Work through the `# TODO` markers. The
matching `solution/` notebook has the reference answer.

Labs 3.1, 3.2, and 3.3 run fully offline with small local models (DistilBERT,
Qwen2.5-0.5B, and distilgpt2). Lab 3.4 embeds and retrieves offline but calls an
LLM API through the shared client for generation and the judge, so set an API
key in Colab secrets or your local `.env` first.

Lab 3.2 downloads about 950 MB for `Qwen/Qwen2.5-0.5B-Instruct` (once per
machine); a smaller `SmolLM2-360M-Instruct` fallback is documented in the lab
for weak wifi. QLoRA and 4-bit quantization stay a concept in this course
because they need a CUDA GPU.

To run locally instead, see the [root README](../README.md) for environment
setup.

## Demos and exercise

- [`demos/`](demos/): instructor demo scripts for each session, as `.py` files
  plus matching Colab notebooks. Every demo runs without an API key.
- [`exercise/`](exercise/): a self-paced Day 3 wrap-up that revisits all four
  sessions in one notebook, with a ready-to-use prompt for each step.
