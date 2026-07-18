"""
Demo: Embeddings & Similarity Search
Day 3 — Session 2

Embeds 5 sentences, queries with a related question, and
displays distance scores to show how similarity search works.
depends on FAISS for the final part, so if you don't have it installed,
run:
pip install faiss-cpu

Run: python3 day3/demos/demo-embeddings.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import numpy as np
from shared import get_embeddings, show_config


# Sentences to embed
SENTENCES = [
    "Python uses indentation to define code blocks.",
    "The capital of France is Paris.",
    "FAISS is a library for efficient similarity search.",
    "Machine learning models learn patterns from data.",
    "The quick brown fox jumps over the lazy dog.",
]

# Queries to test
QUERIES = [
    "How does Python structure its code?",
    "What city is the capital of France?",
    "How do you search for similar vectors?",
    "What is deep learning?",
    "Tell me about animals jumping over things.",
]


def embed_texts(texts):
    """Embed a list of texts via the shared, provider-agnostic client.

    Routes through whatever LLM_PROVIDER is set in .env (openai, gemini,
    claude, or the azure corporate gateway).
    """
    return get_embeddings(texts)


def cosine_similarity(a, b):
    """Compute cosine similarity between two vectors."""
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def demo_embedding_basics():
    """Show what embeddings look like."""
    print("\n" + "=" * 60)
    print("📌 Part 1: What Do Embeddings Look Like?")
    print("=" * 60)

    sample = "Hello, world!"
    embedding = embed_texts([sample])[0]

    print(f"\nText: '{sample}'")
    print(f"Dimensions: {len(embedding)}")
    print(f"First 10 values: {[round(v, 4) for v in embedding[:10]]}")
    print(f"Min: {min(embedding):.4f}, Max: {max(embedding):.4f}")
    print(f"Magnitude: {np.linalg.norm(embedding):.4f}")


def demo_similarity_matrix():
    """Show pairwise similarity between all sentences."""
    print("\n" + "=" * 60)
    print("📌 Part 2: Pairwise Similarity Between Sentences")
    print("=" * 60)

    print("\nEmbedding sentences...")
    embeddings = embed_texts(SENTENCES)

    # Print short labels
    labels = [f"S{i+1}" for i in range(len(SENTENCES))]
    for i, (label, sentence) in enumerate(zip(labels, SENTENCES)):
        print(f"  {label}: {sentence[:60]}")

    # Compute similarity matrix
    print(f"\n{'':>4}", end="")
    for label in labels:
        print(f"{label:>8}", end="")
    print()

    for i, label_i in enumerate(labels):
        print(f"{label_i:>4}", end="")
        for j in range(len(labels)):
            sim = cosine_similarity(embeddings[i], embeddings[j])
            print(f"{sim:>8.3f}", end="")
        print()


def demo_query_search():
    """Show how a query matches against the sentence corpus."""
    print("\n" + "=" * 60)
    print("📌 Part 3: Query → Similarity Search")
    print("=" * 60)

    print("\nEmbedding corpus and queries...")
    sentence_embeddings = embed_texts(SENTENCES)
    query_embeddings = embed_texts(QUERIES)

    for q_idx, query in enumerate(QUERIES):
        print(f"\n🔍 Query: \"{query}\"")

        # Compute similarity to all sentences
        scores = []
        for s_idx, sentence in enumerate(SENTENCES):
            sim = cosine_similarity(query_embeddings[q_idx],
                                    sentence_embeddings[s_idx])
            scores.append((sim, sentence))

        # Sort by similarity (highest first)
        scores.sort(reverse=True)

        for rank, (sim, sentence) in enumerate(scores):
            marker = "✅" if rank == 0 else "  "
            bar = "█" * int(sim * 30)
            print(f"  {marker} {sim:.3f} {bar} {sentence[:55]}")


def demo_faiss_search():
    """Demonstrate FAISS index search."""
    print("\n" + "=" * 60)
    print("📌 Part 4: FAISS Vector Search")
    print("=" * 60)

    try:
        import faiss
    except ImportError:
        print("⚠️  faiss-cpu not installed. Run: pip install faiss-cpu")
        return

    print("\nBuilding FAISS index...")
    sentence_embeddings = embed_texts(SENTENCES)
    dimension = len(sentence_embeddings[0])

    # Build index
    index = faiss.IndexFlatL2(dimension)
    vectors = np.array(sentence_embeddings, dtype=np.float32)
    index.add(vectors)
    print(f"Index built: {index.ntotal} vectors, {dimension} dimensions")

    # Search with each query
    query_embeddings = embed_texts(QUERIES)

    for query, q_emb in zip(QUERIES, query_embeddings):
        q_vec = np.array([q_emb], dtype=np.float32)
        distances, indices = index.search(q_vec, k=3)

        print(f"\n🔍 Query: \"{query}\"")
        print(f"   Top-3 results:")
        for rank in range(3):
            idx = indices[0][rank]
            dist = distances[0][rank]
            print(f"   {rank+1}. [L2={dist:.4f}] {SENTENCES[idx][:55]}")


def main():
    show_config()
    print("\n🔢 Demo: Embeddings & Similarity Search")

    demo_embedding_basics()
    input("\n⏎  Press Enter for the next part...")

    demo_similarity_matrix()
    input("\n⏎  Press Enter for the next part...")

    demo_query_search()
    input("\n⏎  Press Enter for the next part...")

    demo_faiss_search()

    print("\n" + "=" * 60)
    print("📊 Summary:")
    print("   1. Embeddings are high-dimensional vectors (1536-d)")
    print("   2. Cosine similarity measures semantic closeness")
    print("   3. FAISS enables fast nearest-neighbor search")
    print("   4. The best match for a query is the most similar vector")
    print("=" * 60)
    print("\n✅ Demo complete!")


if __name__ == "__main__":
    main()
