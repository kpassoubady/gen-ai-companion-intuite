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
    # TODO: Implement document loading
    # 1. List all .md files in docs_dir
    # 2. Read each file
    # 3. Return a list of dicts: {"filename": "...", "content": "..."}

    return []  # TODO: replace


# ---------------------------------------------------------------------------
# Step 2: Chunk documents
# ---------------------------------------------------------------------------
def chunk_documents(documents, chunk_size=500, overlap=50):
    """Chunk documents and preserve source metadata."""
    # TODO: Implement chunking with metadata
    # 1. For each document, split content into chunks
    # 2. Each chunk should carry: text, source filename, chunk_id
    # 3. Use overlapping chunks to avoid cutting mid-sentence

    return []  # TODO: replace


# ---------------------------------------------------------------------------
# Step 3: Embed and index
# ---------------------------------------------------------------------------
def embed_texts(texts):
    """Embed a list of texts via the shared, provider-agnostic client."""
    # TODO: Implement embedding
    # 1. Call get_embeddings(texts)
    # 2. Return as a list of lists

    return []  # TODO: replace


def build_index(embeddings):
    """Build a FAISS index from a list of embeddings."""
    # TODO: Implement FAISS index building
    # 1. Determine the dimension from the first embedding
    # 2. Create a faiss.IndexFlatL2 index
    # 3. Add all vectors to the index
    # 4. Return the index

    return None  # TODO: replace


# ---------------------------------------------------------------------------
# Step 4: Retrieve
# ---------------------------------------------------------------------------
def retrieve(query, index, chunks, k=3):
    """Embed the query, search the index, return top-k chunks."""
    # TODO: Implement retrieval
    # 1. Embed the query
    # 2. Search the FAISS index for k nearest neighbors
    # 3. Return the matching chunks with their scores

    return []  # TODO: replace


# ---------------------------------------------------------------------------
# Step 5: Generate with RAG
# ---------------------------------------------------------------------------
def build_rag_prompt(query, retrieved_chunks):
    """Build a prompt with retrieved context and citation instructions."""
    # TODO: Implement prompt building
    # 1. Format the retrieved chunks with source labels
    # 2. Create a system message instructing the model to answer
    #    ONLY from the provided context and cite sources
    # 3. Return the messages list

    return []  # TODO: replace


def rag_query(query, index, chunks, k=3):
    """Full RAG pipeline: retrieve → augment → generate."""
    # TODO: Wire the full pipeline together
    # 1. Retrieve relevant chunks
    # 2. Build the RAG prompt
    # 3. Get the completion
    # 4. Return answer + sources

    return {"answer": "TODO: Implement RAG query", "sources": []}


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
