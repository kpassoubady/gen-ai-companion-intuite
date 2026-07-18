# Lab 3.4 - Build an End-to-End RAG Pipeline

**Day 3 - Session 3**

## Objectives

1. Chunk and embed a small knowledge base and index it with FAISS.
2. Retrieve the top chunks for a question and answer with a grounded prompt.
3. Score the answers with an LLM-as-a-judge over a few golden Q&A pairs.

## Setup

Run in Google Colab (recommended): open `start/lab3_4_rag.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

Retrieval runs offline with a local embedding model
(`all-MiniLM-L6-v2`). Generation and the judge call an LLM API through the
shared client, so provide a key one of these ways:

- **Colab:** add `OPENAI_API_KEY` as a Colab secret, or type it when prompted.
- **Local:** copy `.env.example` to `.env` and set your provider and key. See the
  [root README](../../README.md).

Generation uses the `mini` tier to keep cost low. Runs on CPU; no GPU needed.

## Instructions

1. Open `start/lab3_4_rag.ipynb`.
2. Fill in each `# TODO`: build the FAISS index, search it in `retrieve`, and
   build the grounded prompt in `rag_answer`.
3. Run every cell. Grounded questions come back with a citation; the
   mobile-app question is declined because the fact is not in the knowledge
   base. The judge should mark all three golden cases faithful and correct.
4. Try the stretch goals: agentic RAG with smolagents tools, a Chroma index, or
   a different embedding model or chunk size.

## Getting Stuck?

The full working code is in `solution/lab3_4_rag.ipynb`, with the expected
behavior described in the final markdown cell. This lab uses FAISS as the local
vector store; the concept doc shows the Chroma equivalent.
