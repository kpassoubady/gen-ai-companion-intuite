# Capstone - Small Business Finance Assistant

**Day 3 - Session 4**

> **Requires an API key.** Generation and the judge call a hosted LLM through
> the shared client. No key? Use the no-key version at
> [`../capstone_nokey/`](../capstone_nokey/), which builds the same assistant on
> a small local model.

Build a retrieval-augmented assistant that answers small-business finance
questions over a mock QuickBooks and TurboTax help knowledge base. Everyone
ships the base assistant; then pick up the tiered stretch goals as time allows.

All data in `data/` is synthetic mock data. There is no real customer or
financial data.

## Objectives

1. Load, chunk, embed, and index a help knowledge base with FAISS.
2. Answer questions grounded in the retrieved articles, with citations.
3. Extend the assistant with agentic tools, evaluation, and fine-tuning.

## Setup

Run in Google Colab (recommended): open `start/capstone.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

Retrieval and fine-tuning run offline with small local models. Generation and
the judge call an LLM API through the shared client, so provide a key one of
these ways:

- **Colab:** add `OPENAI_API_KEY` as a Colab secret, or type it when prompted.
- **Local:** copy `.env.example` to `.env` and set your provider and key. See the
  [root README](../README.md).

Runs on CPU; no GPU needed.

## The build

**Base (everyone).** Fill in the `# TODO` markers in `start/capstone.ipynb`:
build the FAISS index, search it in `retrieve`, and build the grounded prompt in
`rag_answer`. Run every cell. The assistant should answer the finance questions
with a source citation and decline the question it has no data for.

**Stretch goals (pick up in order as time allows).**

1. **Agentic RAG.** Give a smolagents agent a knowledge-base search tool and an
   `invoice_total` tool that adds sales tax, so it can search then compute.
2. **LLM-as-a-judge.** Score the assistant on the golden Q&A pairs in
   `data/golden_qa.json` for faithfulness and correctness.
3. **Compare chunking.** Rebuild the index with smaller chunks and compare which
   source each question retrieves.
4. **LoRA ticket router.** Adapt Lab 3.2 to train a LoRA classifier on
   `data/support_tickets.json` that routes tickets into billing, payroll,
   tax_filing, or integrations.

## Data

| File | Contents |
| :--- | :--- |
| `data/*.md` | Mock QuickBooks and TurboTax help articles (the knowledge base) |
| `data/golden_qa.json` | Golden question and answer pairs for evaluation |
| `data/support_tickets.json` | Labeled tickets for the LoRA routing stretch |

## Getting Stuck?

The full working code is in `solution/capstone.ipynb`, with the expected
behavior described in the final markdown cell.
