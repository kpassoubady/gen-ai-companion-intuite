# Capstone (No Key) - Small Business Finance Assistant

**Day 3 - Session 4**

This is the no-key version of the [Capstone](../capstone/). Use it if you do not
have an LLM API key. It builds the same retrieval-augmented finance assistant
over a mock QuickBooks and TurboTax help knowledge base.

All data in `../capstone/data/` is synthetic mock data. There is no real
customer or financial data.

## How this runs without an API key

Retrieval and fine-tuning already run offline. For generation and the judge this
version swaps the hosted LLM for a small local model, `google/flan-t5-base`, that
downloads once (about 1 GB) and runs on CPU. The agentic stretch replaces the LLM
planner with a scripted planner so the tool loop stays visible and deterministic.
Everything else matches the API capstone; only the call sites change
(`generate(...)` and a scripted planner instead of `get_completion(...)` and a
`LiteLLMModel` agent). A small local model is weaker than a hosted one, so answers
are terser and the judge is stricter.

## Objectives

1. Load, chunk, embed, and index a help knowledge base with FAISS.
2. Answer questions grounded in the retrieved articles, with citations.
3. Extend the assistant with an agentic tool loop, evaluation, and fine-tuning.

## Setup

Run in Google Colab (recommended): open `start/capstone_nokey.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies. The setup
cell downloads the local model and finds `capstone/data/` (cloning the companion
repo on Colab). No API key and no `.env` needed. Runs on CPU; no GPU needed.

## The build

**Base (everyone).** Fill in the `# TODO` markers in `start/capstone_nokey.ipynb`:
build the FAISS index, search it in `retrieve`, and generate the grounded answer
in `rag_answer`. Run every cell. The assistant should answer the finance
questions with a source citation and decline the question it has no data for.

**Stretch goals (pick up in order as time allows).**

1. **Agentic RAG.** Give a hand-written tool loop a knowledge-base search tool
   and an `invoice_total` tool that adds sales tax, driven by a scripted planner
   that searches then computes.
2. **LLM-as-a-judge.** Use the local model to score the assistant on the golden
   Q&A pairs in `data/golden_qa.json`.
3. **Compare chunking.** Rebuild the index with smaller chunks and compare which
   source each question retrieves.
4. **LoRA ticket router.** Adapt Lab 3.2 to train a LoRA classifier on
   `data/support_tickets.json` that routes tickets into billing, payroll,
   tax_filing, or integrations.

## Data

The knowledge base and evaluation files are shared with the API capstone in
[`../capstone/data/`](../capstone/data/):

| File | Contents |
| :--- | :--- |
| `data/*.md` | Mock QuickBooks and TurboTax help articles (the knowledge base) |
| `data/golden_qa.json` | Golden question and answer pairs for evaluation |
| `data/support_tickets.json` | Labeled tickets for the LoRA routing stretch |

## Getting Stuck?

The full working code is in `solution/capstone_nokey.ipynb`, with the expected
behavior described in the final markdown cell.
