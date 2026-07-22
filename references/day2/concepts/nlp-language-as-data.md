# NLP: Understanding Language as Data

Reference for how text becomes numbers a model can use: tokenization, vectorization, and embeddings.

---

## What NLP Is

Natural language processing is the set of techniques that let software read, interpret, and generate human language. The same pipeline underlies classification, extraction, search, translation, and generation: turn text into numbers, feed a model, and read the output.

## Tokenization

A token is a chunk of text the model treats as one unit, mapped to an integer ID. Tokens can be words, subwords, or a few characters. A rough rule for English is that one token is about four characters.

Word-level splitting fails because vocabularies grow huge, rare words become unknown tokens, and typos have no entry. Subword tokenization fixes all three by building any word from known pieces.

| Method | Used by | Idea |
| :--- | :--- | :--- |
| **Byte Pair Encoding (BPE)** | GPT, Llama | Start from characters, merge the most frequent pairs |
| **WordPiece** | BERT | Merge pairs that most improve the training likelihood |

Both produce subwords, so no word is ever truly out of vocabulary.

Token counts matter in practice. APIs bill per token, context windows are measured in tokens, some languages use more tokens per word than English, and code spends tokens on whitespace and symbols.

## Vectorization with Bag-of-Words

Bag-of-words counts how often each word appears and ignores order. Each document becomes a long vector with one slot per vocabulary word.

It has three weaknesses:

- **No order:** "dog bites man" and "man bites dog" look identical.
- **No meaning:** "car" and "automobile" are unrelated slots.
- **Sparse and large:** vectors are mostly zeros across thousands of entries.

## Embeddings

An embedding is a dense vector, a few hundred numbers, learned so that similar meanings land near each other. "king" and "queen" sit close together while "king" and "banana" sit far apart. The vector is learned from context in large amounts of text, so similar text produces a similar vector.

### Cosine Similarity

Cosine similarity measures the angle between two vectors:

- Near 1: vectors point the same way (very similar).
- Near 0: unrelated.
- Near -1: opposite.

It ignores vector length and focuses on direction, which is what we want when comparing meaning.

### Similarity Search

Embed the query and every document, then rank documents by cosine similarity to the query. This one idea powers semantic search, recommendations, and retrieval-augmented generation, which the Day 3 RAG session builds on directly.
