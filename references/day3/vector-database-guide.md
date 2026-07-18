# Vector Database Guide

A reference for working with vector databases in RAG applications.

---

## What Is a Vector Database?

A database optimized for storing high-dimensional vectors and performing fast similarity search. Unlike traditional databases that match exact values, vector databases find the "closest" entries by distance.

---

## FAISS (Facebook AI Similarity Search)

The vector store used in this course. A fast, in-memory library for similarity search.

### Installation

```bash
pip install faiss-cpu
```

### Quick Start

```python
import faiss
import numpy as np

# 1. Create an index
dimension = 1536  # must match embedding dimensions
index = faiss.IndexFlatL2(dimension)  # exact L2 distance search

# 2. Add vectors
vectors = np.array(list_of_embeddings, dtype=np.float32)
index.add(vectors)
print(f"Vectors in index: {index.ntotal}")

# 3. Search
query = np.array([query_embedding], dtype=np.float32)
distances, indices = index.search(query, k=5)

# distances[0] = [0.12, 0.34, 0.56, 0.78, 0.91]  (L2 distances)
# indices[0]   = [7, 3, 12, 0, 22]                  (vector IDs)
```

### Index Types

| Index | Speed | Accuracy | Memory | Best For |
|:------|:------|:---------|:-------|:---------|
| `IndexFlatL2` | Slow (brute-force) | Exact | High | < 100K vectors |
| `IndexFlatIP` | Slow (brute-force) | Exact | High | Cosine similarity (normalized) |
| `IndexIVFFlat` | Fast (approximate) | Good | Medium | 100K-10M vectors |
| `IndexHNSW` | Very fast | Very good | High | Production workloads |

### Saving and Loading

```python
# Save
faiss.write_index(index, "my_index.faiss")

# Load
index = faiss.read_index("my_index.faiss")
```

### Using Cosine Similarity with FAISS

FAISS `IndexFlatL2` uses L2 (Euclidean) distance. For cosine similarity:

```python
# Normalize vectors before adding to index
def normalize(vectors):
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / norms

# Use IndexFlatIP (inner product) with normalized vectors
# Inner product of normalized vectors = cosine similarity
index = faiss.IndexFlatIP(dimension)
index.add(normalize(vectors))

# Search (higher score = more similar)
distances, indices = index.search(normalize(query), k=5)
```

---

## Chroma

An embedded vector database with a simpler API. Handles embedding automatically if configured.

### Quick Start

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("my_docs")

# Add documents (Chroma can auto-embed if you configure an embedding function)
collection.add(
    documents=["doc1 text", "doc2 text", "doc3 text"],
    metadatas=[{"source": "file1"}, {"source": "file2"}, {"source": "file3"}],
    ids=["id1", "id2", "id3"],
)

# Query
results = collection.query(
    query_texts=["search query"],
    n_results=3,
)
print(results["documents"])   # matched texts
print(results["metadatas"])   # metadata
print(results["distances"])   # similarity scores
```

### When to Use Chroma over FAISS

| FAISS | Chroma |
|:------|:-------|
| Just vectors (you manage metadata) | Vectors + documents + metadata |
| Numpy arrays | Simple Python API |
| Manual embedding | Optional auto-embedding |
| Pure library (no persistence by default) | Built-in persistence |
| Maximum speed | Convenience |

---

## Metadata Management

Vector databases store vectors, but you need metadata (source file, chunk ID, section) alongside them. Two approaches:

### Approach 1: Parallel Lists (FAISS)

```python
# FAISS only stores vectors. Keep metadata in a parallel list.
chunks = [
    {"text": "...", "source": "file1.md", "chunk_id": 0},
    {"text": "...", "source": "file1.md", "chunk_id": 1},
    {"text": "...", "source": "file2.md", "chunk_id": 0},
]

# FAISS index position i corresponds to chunks[i]
distances, indices = index.search(query, k=3)
for idx in indices[0]:
    print(chunks[idx]["source"], chunks[idx]["text"][:50])
```

### Approach 2: Built-in Metadata (Chroma, Pinecone)

```python
# Chroma stores metadata alongside vectors
collection.add(
    documents=[chunk["text"] for chunk in chunks],
    metadatas=[{"source": chunk["source"]} for chunk in chunks],
    ids=[f"chunk_{i}" for i in range(len(chunks))],
)
```

---

## Distance Metrics

| Metric | Formula | Range | Lower = |
|:-------|:--------|:------|:--------|
| **L2 (Euclidean)** | sqrt(sum((a-b)^2)) | 0 to inf | More similar |
| **Cosine Similarity** | dot(a,b) / (norm(a)*norm(b)) | -1 to 1 | (Higher = more similar) |
| **Inner Product** | dot(a,b) | -inf to inf | (Higher = more similar) |

> For normalized vectors, L2 distance and cosine similarity give equivalent rankings.

---

## Production Considerations

| Concern | Recommendation |
|:--------|:--------------|
| **Persistence** | Save FAISS index to disk; use Chroma persistent mode |
| **Updates** | Rebuild index when docs change (FAISS); upsert in Chroma/Pinecone |
| **Scale** | < 100K → FAISS; 100K-1M → Chroma; 1M+ → Pinecone/Weaviate |
| **Filtering** | Use Chroma/Pinecone metadata filters; FAISS has no built-in filtering |
| **Backup** | Persist index files alongside your application |
