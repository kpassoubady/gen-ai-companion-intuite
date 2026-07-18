# Lab 2.1 - Find Similar Documents with Embeddings

**Day 2 - Session 1**

## Objectives

1. Embed a small document collection with a sentence-transformers model.
2. Rank documents by cosine similarity to a query.
3. Compare semantic search against plain keyword matching.

## Setup

Run in Google Colab (recommended): open `start/lab2_1_similarity.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

To run locally instead, activate the repo virtual environment and install
requirements. See the [root README](../../README.md).

This lab uses sentence-transformers locally. No API key and no GPU needed.

## Instructions

1. Open `start/lab2_1_similarity.ipynb`.
2. Fill in each `# TODO`: embed the documents, embed the query, score with a dot
   product, and count keyword overlap.
3. Run every cell. The password query should return the password and
   account-recovery documents first, and semantic search should beat keyword
   search on the "locked out" query.
4. Try the stretch goals: cluster the documents with KMeans, or compare a second
   embedding model.

## Getting Stuck?

The full working code is in `solution/lab2_1_similarity.ipynb`.
