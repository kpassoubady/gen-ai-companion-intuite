"""
Lab 3.2 — End-to-End RAG Chatbot
Day 3 — Session 3

Goal: Build a complete RAG system that answers questions about a knowledge base.

Steps:
1. Load markdown docs from day3/knowledge-base/
2. Chunk the documents with metadata
3. Embed chunks and store in FAISS
4. Build a query loop: user asks, system retrieves + generates
5. Cite sources in every answer

Stretch goals:
- Experiment with chunk_size (200, 500, 1000) — compare retrieval quality
- Add a relevance threshold — don't use chunks below score X
- Combine RAG with conversation history for multi-turn RAG

Run: python3 day3/labs/lab3_2_rag_chatbot.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import os
import numpy as np
from shared import get_completion, get_embeddings, show_config


# ---------------------------------------------------------------------------
# Step 1: Load documents
# ---------------------------------------------------------------------------
def load_documents(docs_dir):
    """Load all .md files from a directory."""
    documents = []
    for filename in sorted(os.listdir(docs_dir)):
        if filename.endswith(".md"):
            filepath = os.path.join(docs_dir, filename)
            with open(filepath, "r") as f:
                documents.append({
                    "filename": filename,
                    "content": f.read(),
                })
    return documents


# ---------------------------------------------------------------------------
# Step 2: Chunk documents
# ---------------------------------------------------------------------------
def chunk_documents(documents, chunk_size=500, overlap=50):
    """Chunk documents and preserve source metadata."""
    chunks = []
    for doc in documents:
        text = doc["content"]
        start = 0
        chunk_num = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]
            chunks.append({
                "text": chunk_text,
                "source": doc["filename"],
                "chunk_id": chunk_num,
            })
            start = end - overlap
            chunk_num += 1
    return chunks


# ---------------------------------------------------------------------------
# Step 3: Embed and index
# ---------------------------------------------------------------------------
def embed_texts(texts):
    """Embed a list of texts via the shared, provider-agnostic client."""
    return get_embeddings(texts)


def build_index(embeddings):
    """Build a FAISS index from a list of embeddings."""
    import faiss
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    vectors = np.array(embeddings, dtype=np.float32)
    index.add(vectors)
    return index


# ---------------------------------------------------------------------------
# Step 4: Retrieve
# ---------------------------------------------------------------------------
def retrieve(query, index, chunks, k=3):
    """Embed the query, search the index, return top-k chunks."""
    query_embedding = embed_texts([query])[0]
    query_vector = np.array([query_embedding], dtype=np.float32)
    distances, indices = index.search(query_vector, k)

    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(chunks):  # valid index
            results.append({
                **chunks[idx],
                "score": float(distances[0][i]),
            })
    return results


# ---------------------------------------------------------------------------
# Step 5: Generate with RAG
# ---------------------------------------------------------------------------
def build_rag_prompt(query, retrieved_chunks):
    """Build a prompt with retrieved context and citation instructions."""
    context = "\n\n---\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}"
        for c in retrieved_chunks
    )

    messages = [
        {"role": "system", "content":
            "Answer the user's question based ONLY on the provided context. "
            "If the context doesn't contain the answer, say "
            "'I don't have enough information to answer that.' "
            "Always cite your sources using [Source: filename]."},
        {"role": "user", "content":
            f"Context:\n{context}\n\n---\n\nQuestion: {query}"},
    ]
    return messages


def rag_query(query, index, chunks, k=3):
    """Full RAG pipeline: retrieve → augment → generate."""
    retrieved = retrieve(query, index, chunks, k=k)
    if not retrieved:
        return {"answer": "No relevant documents found.", "sources": []}

    messages = build_rag_prompt(query, retrieved)
    response = get_completion(messages, temperature=0.0)

    sources = list(set(c["source"] for c in retrieved))
    return {"answer": response, "sources": sources}


# ---------------------------------------------------------------------------
# Main: Interactive RAG chat loop
# ---------------------------------------------------------------------------
def main():
    show_config()
    print("\n🔍 RAG Chatbot — Lab 3.2")
    print("Loading knowledge base...\n")

    # Step 1: Load
    docs_dir = os.path.join(os.path.dirname(__file__), "..", "knowledge-base")
    docs_dir = os.path.normpath(docs_dir)
    documents = load_documents(docs_dir)
    print(f"📄 Loaded {len(documents)} documents")

    if not documents:
        print("⚠️  No documents found. Check day3/knowledge-base/ directory.")
        print("   Make sure .md files exist in that directory.")
        return

    # Step 2: Chunk
    chunks = chunk_documents(documents)
    print(f"✂️  Created {len(chunks)} chunks")

    if not chunks:
        print("⚠️  No chunks created. Implement chunk_documents().")
        return

    # Step 3: Embed and index
    print("🔢 Embedding chunks...")
    texts = [chunk["text"] for chunk in chunks]
    embeddings = embed_texts(texts)

    if not embeddings:
        print("⚠️  No embeddings generated. Implement embed_texts().")
        return

    index = build_index(embeddings)
    if index is None:
        print("⚠️  Index not built. Implement build_index().")
        return

    print(f"🗄️  FAISS index ready: {index.ntotal} vectors")
    print(f"\nType your questions. Type 'quit' to exit.\n")
    print("-" * 50)

    # Step 4: Interactive query loop
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        # Run RAG query
        result = rag_query(user_input, index, chunks)

        print(f"\n🤖 Bot: {result['answer']}")
        if result["sources"]:
            print(f"\n📚 Sources: {', '.join(result['sources'])}")

    print("\n✅ Lab 3.2 complete!")


if __name__ == "__main__":
    main()
