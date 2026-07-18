"""
Lab 3.3 — Flask API for the RAG Chatbot
Day 3 — Session 4

Goal: Wrap the RAG chatbot from Lab 3.2 in a Flask API.

Endpoints:
  POST /api/chat    — {"message": "..."} → {"answer": "...", "sources": [...]}
  GET  /api/health  — {"status": "ok", "chunks_loaded": N}

Stretch goals:
  - Add session-based conversation history
  - Add response caching for repeated queries
  - Add GET /api/sources listing all indexed documents

Test with:
  curl -X POST http://localhost:5001/api/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "What Python data structures are used for key-value pairs?"}'

Run: python3 day3/labs/lab3_3_flask_api.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import os
import hashlib
import numpy as np

from flask import Flask, request, jsonify

from shared import get_completion, get_embeddings, show_config


# ---------------------------------------------------------------------------
# RAG components (reuse from Lab 3.2 or implement inline)
# ---------------------------------------------------------------------------

def load_documents(docs_dir):
    """Load all .md files from a directory."""
    # TODO: Copy or import your implementation from Lab 3.2
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


def chunk_documents(documents, chunk_size=500, overlap=50):
    """Chunk documents and preserve source metadata."""
    # TODO: Copy or import your implementation from Lab 3.2
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


def embed_texts(texts):
    """Embed a list of texts via the shared, provider-agnostic client."""
    # TODO: Copy or import your implementation from Lab 3.2
    return get_embeddings(texts)


def build_index(embeddings):
    """Build a FAISS index from embeddings."""
    # TODO: Copy or import your implementation from Lab 3.2
    import faiss
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    vectors = np.array(embeddings, dtype=np.float32)
    index.add(vectors)
    return index


def retrieve(query, index, chunks, k=3):
    """Embed query and search FAISS index."""
    # TODO: Copy or import your implementation from Lab 3.2
    import faiss
    query_embedding = embed_texts([query])[0]
    query_vector = np.array([query_embedding], dtype=np.float32)
    distances, indices = index.search(query_vector, k)
    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(chunks):
            results.append({**chunks[idx], "score": float(distances[0][i])})
    return results


def rag_query(query, index, chunks, k=3):
    """Full RAG pipeline: retrieve → augment → generate."""
    # TODO: Copy or import your implementation from Lab 3.2
    retrieved = retrieve(query, index, chunks, k=k)
    if not retrieved:
        return {"answer": "No relevant documents found.", "sources": []}

    context = "\n\n---\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}" for c in retrieved
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

    response = get_completion(messages, temperature=0.0)
    sources = list(set(c["source"] for c in retrieved))
    return {"answer": response, "sources": sources}


# ---------------------------------------------------------------------------
# Flask app
# ---------------------------------------------------------------------------

app = Flask(__name__)

# Global state (initialized in main)
INDEX = None
CHUNKS = []
DOCUMENTS = []

# Optional: response cache
CACHE = {}


@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint."""
    # TODO: Return status and number of chunks loaded

    return jsonify({"status": "TODO"})


@app.route("/api/chat", methods=["POST"])
def chat():
    """Chat endpoint — accepts a message, returns RAG-powered answer."""
    # TODO: Implement the chat endpoint
    # 1. Parse the JSON body and extract "message"
    # 2. Validate the input (return 400 if missing)
    # 3. Run rag_query()
    # 4. Return the answer and sources as JSON
    # 5. Handle errors gracefully

    return jsonify({"error": "TODO: Implement chat endpoint"}), 501


# Stretch: List all indexed document sources
@app.route("/api/sources", methods=["GET"])
def sources():
    """List all documents in the knowledge base."""
    # TODO (Stretch): Return the list of source documents

    return jsonify({"sources": [], "count": 0})


# ---------------------------------------------------------------------------
# Initialization
# ---------------------------------------------------------------------------

def initialize_rag():
    """Load documents, build embeddings, and create FAISS index."""
    global INDEX, CHUNKS, DOCUMENTS

    docs_dir = os.path.join(os.path.dirname(__file__), "..", "knowledge-base")
    docs_dir = os.path.normpath(docs_dir)

    print("📄 Loading documents...")
    DOCUMENTS = load_documents(docs_dir)
    print(f"   Loaded {len(DOCUMENTS)} documents")

    if not DOCUMENTS:
        print("⚠️  No documents found in", docs_dir)
        return False

    print("✂️  Chunking...")
    CHUNKS = chunk_documents(DOCUMENTS)
    print(f"   Created {len(CHUNKS)} chunks")

    print("🔢 Embedding...")
    texts = [chunk["text"] for chunk in CHUNKS]
    embeddings = embed_texts(texts)
    print(f"   Generated {len(embeddings)} embeddings")

    print("🗄️  Building FAISS index...")
    INDEX = build_index(embeddings)
    print(f"   Index ready: {INDEX.ntotal} vectors")

    return True


def main():
    show_config()
    print("\n🌐 Flask RAG API — Lab 3.3\n")

    if not initialize_rag():
        print("❌ Failed to initialize RAG. Check knowledge base directory.")
        return

    print(f"\n🚀 Starting Flask server...")
    print(f"   POST http://localhost:5001/api/chat")
    print(f"   GET  http://localhost:5001/api/health")
    print(f"\nTest with:")
    print(f'   curl -X POST http://localhost:5001/api/chat \\')
    print(f'     -H "Content-Type: application/json" \\')
    print(f'     -d \'{{"message": "What is a Python dictionary?"}}\'\n')

    app.run(debug=False, port=5001)


if __name__ == "__main__":
    main()
