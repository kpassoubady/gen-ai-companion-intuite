# RAG Architecture Reference

A reference for building Retrieval-Augmented Generation (RAG) systems.

---

## What Is RAG?

RAG grounds LLM responses in retrieved documents to reduce hallucination. Instead of relying solely on the model's training data, RAG fetches relevant information at query time and injects it into the prompt.

---

## The Two Pipelines

### Ingestion Pipeline (runs once or on updates)

```
Documents → Chunking → Embedding Model → Vector Store
```

1. **Load** documents (PDF, Markdown, HTML, etc.)
2. **Chunk** into smaller pieces (200-500 tokens)
3. **Embed** each chunk into a vector
4. **Store** vectors + metadata in a vector database

### Query Pipeline (runs every user question)

```
User Query → Embed → Search → Retrieve Top-K → Augment Prompt → LLM → Answer
```

1. **Embed** the user query
2. **Search** the vector store for similar chunks
3. **Retrieve** the top-K most relevant chunks
4. **Augment** the prompt with retrieved context
5. **Generate** an answer grounded in the context

---

## Chunking

### Strategies

| Strategy | How It Works | Best For |
|:---------|:-----------|:---------|
| **Fixed size** | Split every N characters/tokens | Simple, predictable |
| **Semantic** | Split by paragraphs, sections, headers | Structured documents |
| **Overlapping** | Fixed size with N% overlap | Preventing mid-sentence cuts |

### Guidelines

| Parameter | Recommendation |
|:----------|:--------------|
| Chunk size | 200-500 tokens |
| Overlap | 10-20% of chunk size |
| Split boundaries | Paragraphs, headers, sentences |
| Metadata | Source file, page, section, chunk_id |

### Code

```python
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks
```

---

## Embeddings

### Models

| Model | Provider | Dimensions | Cost/1M tokens |
|:------|:---------|:-----------|:---------------|
| `text-embedding-3-small` | OpenAI | 1536 | $0.02 |
| `text-embedding-3-large` | OpenAI | 3072 | $0.13 |
| `embedding-001` | Google | 768 | Free tier |

### Generating Embeddings

```python
import litellm

response = litellm.embedding(
    model="text-embedding-3-small",
    input=["text to embed"]
)
vector = response.data[0]["embedding"]  # list of 1536 floats
```

### Cosine Similarity

```python
import numpy as np

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
```

| Score | Meaning |
|:------|:--------|
| 0.90+ | Very similar |
| 0.70-0.89 | Related |
| 0.50-0.69 | Somewhat related |
| < 0.50 | Unrelated |

---

## Vector Stores

### FAISS (recommended for this course)

```python
import faiss
import numpy as np

# Build
dimension = 1536
index = faiss.IndexFlatL2(dimension)
vectors = np.array(embeddings, dtype=np.float32)
index.add(vectors)

# Search
query_vec = np.array([query_embedding], dtype=np.float32)
distances, indices = index.search(query_vec, k=3)

# Save / Load
faiss.write_index(index, "index.faiss")
index = faiss.read_index("index.faiss")
```

### Comparison

| Database | Type | Best For |
|:---------|:-----|:---------|
| **FAISS** | Library | Prototypes, < 100K vectors |
| **Chroma** | Embedded | Small production |
| **Pinecone** | Cloud | Production at scale |
| **pgvector** | PostgreSQL ext | Teams on Postgres |

---

## RAG Prompt Template

```python
SYSTEM = """Answer the user's question based ONLY on the provided context.
If the context doesn't contain the answer, say
'I don't have enough information to answer that.'
Always cite your sources using [Source: filename]."""

def build_prompt(query, chunks):
    context = "\n\n---\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}" for c in chunks
    )
    return [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": f"Context:\n{context}\n\n---\n\nQuestion: {query}"},
    ]
```

---

## RAG vs Alternatives

| Approach | When to Use | Data Freshness |
|:---------|:-----------|:---------------|
| **Prompt Engineering** | No private data needed | N/A |
| **RAG** | Private/changing data, need citations | Real-time |
| **Fine-Tuning** | Specific style, stable data | Stale after training |

**Rule of thumb:** Try prompt engineering first. Add RAG for private data. Fine-tune only as a last resort.

---

## Common Pitfalls

| Problem | Fix |
|:--------|:----|
| Chunks too large | Reduce to 200-300 tokens |
| Chunks too small | Increase size, add overlap |
| Poor retrieval | Try larger embedding model |
| Too few results | Increase k |
| Too many results | Decrease k, add score threshold |
| No citations | Add citation instruction to system prompt |
| Hallucination despite RAG | Strengthen "ONLY from context" instruction |
