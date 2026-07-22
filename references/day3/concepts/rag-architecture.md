# RAG Architecture

Reference for building Retrieval-Augmented Generation (RAG) systems: the two pipelines, chunking, embeddings, local vector stores (FAISS and Chroma), the RAG prompt, RAG versus fine-tuning, and common pitfalls.

---

## What RAG Is

RAG grounds model responses in retrieved documents to reduce hallucination. Instead of relying on the model's training data alone, the system fetches relevant text at query time and injects it into the prompt. The model answers from that context and can cite it.

## The Two Pipelines

### Ingestion (runs once or on updates)

```
Documents -> Chunking -> Embedding Model -> Vector Store
```

1. Load documents (PDF, Markdown, HTML, and so on).
2. Chunk them into smaller pieces.
3. Embed each chunk into a vector.
4. Store the vectors plus metadata in a vector store.

### Query (runs on every question)

```
Query -> Embed -> Search -> Top-K Chunks -> Build Prompt -> LLM -> Answer
```

1. Embed the user query with the same model used at ingestion.
2. Search the vector store for similar chunks.
3. Retrieve the top-k most relevant chunks.
4. Build a prompt with the retrieved context and the query.
5. Generate an answer grounded in that context.

## Chunking

| Strategy | How it works | Best for |
| :--- | :--- | :--- |
| **Fixed size** | Split every N characters or tokens | Simple, predictable |
| **Semantic** | Split by paragraphs, sections, headers | Structured documents |
| **Overlapping** | Fixed size with an overlap window | Avoiding mid-sentence cuts |

Guidelines: aim for chunks of roughly 200 to 500 tokens with 10 to 20 percent overlap, split on natural boundaries, and store metadata (source file, section, chunk id) for citations.

```python
def chunk_text(text, chunk_size=500, overlap=50):
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks
```

## Embeddings

Choose an embedding model by quality, dimension, cost, and whether it runs locally. For an offline course, a local `sentence-transformers` model works well.

```python
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")  # 384 dims, local
vectors = embedder.encode(["chunk one", "chunk two"])
```

Use the same embedding model for ingestion and queries. Larger models give better retrieval at higher cost and latency.

## Vector Stores (Local)

### FAISS

FAISS is a library for fast similarity search over vectors held in memory. Good for prototypes and small corpora.

```python
import faiss
import numpy as np

index = faiss.IndexFlatL2(384)          # match embedding dimension
index.add(np.array(vectors, dtype=np.float32))

q = np.array([query_vec], dtype=np.float32)
distances, indices = index.search(q, k=3)
```

### Chroma

Chroma is an embedded vector database that stores vectors, documents, and metadata together and persists to disk.

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("docs")
collection.add(documents=chunks, embeddings=vectors.tolist(),
               ids=[f"c{i}" for i in range(len(chunks))])

results = collection.query(query_embeddings=[query_vec], n_results=3)
```

| Store | Type | Best for |
| :--- | :--- | :--- |
| **FAISS** | In-memory library | Prototypes, small corpora |
| **Chroma** | Embedded database | Local apps with metadata and persistence |

## RAG Prompt Template

```python
SYSTEM = """Answer the question using ONLY the provided context.
If the context does not contain the answer, say you do not have enough
information. Cite sources as [Source: filename]."""

def build_messages(query, chunks):
    context = "\n\n---\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}" for c in chunks
    )
    return [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
    ]
```

## RAG vs Fine-Tuning

| Approach | Use when | Data freshness |
| :--- | :--- | :--- |
| **Prompt engineering** | No private data needed | Not applicable |
| **RAG** | Private or changing data, need citations | Current at query time |
| **Fine-tuning** | Fixed style or format, stable data | Frozen at training time |

Rule of thumb: try prompting first, add RAG for private or changing facts, and fine-tune only for a consistent style or format that prompting cannot hold.

## Common Pitfalls

| Problem | Fix |
| :--- | :--- |
| Chunks too large | Reduce to 200 to 300 tokens |
| Chunks too small | Increase size, add overlap |
| Poor retrieval | Try a larger embedding model |
| Too few results | Increase k |
| Too many weak results | Decrease k, add a score threshold |
| No citations | Add a citation instruction to the system prompt |
| Hallucination despite context | Strengthen the "only from context" instruction |
