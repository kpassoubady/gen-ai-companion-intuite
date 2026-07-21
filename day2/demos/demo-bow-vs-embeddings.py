"""
Demo - Bag-of-Words vs Embeddings
Day 2 - Session 1

Goal: Show why bag-of-words misses meaning and how embeddings fix it.

Part 1 builds bag-of-words count vectors with scikit-learn and shows two
problems: word order is lost ("dog bites man" == "man bites dog") and synonyms
are unrelated slots ("car" vs "automobile"). Part 2 embeds the same sentences
with a small sentence-transformers model and ranks them by cosine similarity, so
students see meaning captured as direction in vector space.

No API key needed. The embedding model downloads once (~80 MB), then caches.

Run: python3 day2/demos/demo-bow-vs-embeddings.py
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

DOCS = [
    "dog bites man",
    "man bites dog",
    "I drove my car to work",
    "I drove my automobile to the office",
    "the weather is sunny today",
]


def cosine(a, b):
    """Cosine similarity between two vectors."""
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def demo_bag_of_words():
    """Count vectors lose order and treat synonyms as unrelated."""
    print("\n1. Bag-of-words (scikit-learn CountVectorizer)")
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(DOCS).toarray()
    print(f"  vocabulary: {list(vectorizer.get_feature_names_out())}")

    s = cosine(matrix[0], matrix[1])
    print(f"\n  'dog bites man' vs 'man bites dog' -> cosine {s:.2f}")
    print("  Identical vectors: order is thrown away.")

    s = cosine(matrix[2], matrix[3])
    print(f"\n  'car' sentence vs 'automobile' sentence -> cosine {s:.2f}")
    print("  Low overlap: synonyms are unrelated slots.")


def demo_embeddings():
    """Dense embeddings place similar meaning close together."""
    print("\n\n2. Embeddings (sentence-transformers all-MiniLM-L6-v2)")
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("all-MiniLM-L6-v2")
    vectors = model.encode(DOCS)

    s = cosine(vectors[2], vectors[3])
    print(f"\n  'car' sentence vs 'automobile' sentence -> cosine {s:.2f}")
    print("  High similarity: embeddings capture shared meaning.")

    query = "How do I commute to my job?"
    q_vec = model.encode([query])[0]
    print(f"\n  Similarity search for query: {query!r}")
    scored = sorted(
        ((cosine(q_vec, v), doc) for v, doc in zip(vectors, DOCS)),
        reverse=True,
    )
    for score, doc in scored:
        print(f"    {score:.2f}  {doc}")


def main():
    print("Bag-of-words counts words. Embeddings capture meaning. Compare them.")
    demo_bag_of_words()
    demo_embeddings()
    print("\n\nTakeaway: rank by cosine similarity on embeddings, not word overlap.")


if __name__ == "__main__":
    main()
