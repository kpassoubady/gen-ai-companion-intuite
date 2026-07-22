"""
Demo - Feature Extraction as Transfer Learning
Day 3 - Session 1

Goal: Show that a frozen pre-trained encoder plus a tiny trainable head reaches
good accuracy on a new task without touching the base model weights.

We embed a small labeled set of sentences with a frozen sentence-transformers
model (the "backbone" stays fixed), then train only a logistic-regression head
on those features. This is feature extraction: the base does the heavy lifting,
the head learns the last mile. Full fine-tuning, by contrast, would update every
weight in the encoder.

No API key needed. The embedding model downloads once (~80 MB), then caches.

Run: python3 day3/demos/demo-feature-extraction.py
"""

from sklearn.linear_model import LogisticRegression

# Tiny labeled sentiment set: 1 = positive, 0 = negative.
TRAIN = [
    ("This product is fantastic, I love it", 1),
    ("Best purchase I have made all year", 1),
    ("Absolutely wonderful and easy to use", 1),
    ("The support team was helpful and kind", 1),
    ("Works exactly as described, very happy", 1),
    ("A complete waste of money", 0),
    ("Terrible quality, broke on day one", 0),
    ("I regret buying this, very disappointed", 0),
    ("The worst experience with any app", 0),
    ("Slow, buggy, and frustrating to use", 0),
]

TEST = [
    "I am thrilled with how well this works",
    "This was a huge letdown and a waste",
    "Delightful and dependable, highly recommend",
    "Awful, do not buy this at all",
]


def main():
    print("Feature extraction: freeze the encoder, train only a small head.\n")
    print("Loading frozen encoder (downloads once, then cached)...")
    from sentence_transformers import SentenceTransformer

    encoder = SentenceTransformer("all-MiniLM-L6-v2")

    texts = [t for t, _ in TRAIN]
    labels = [y for _, y in TRAIN]

    # The frozen backbone turns text into fixed feature vectors.
    train_features = encoder.encode(texts)
    print(f"Encoder frozen. Feature vector size: {train_features.shape[1]}")

    # Only this small head is trained. The encoder never updates.
    head = LogisticRegression(max_iter=1000)
    head.fit(train_features, labels)
    head_params = train_features.shape[1] + 1  # weights + bias
    print(f"Trained head parameters: {head_params} (encoder stays frozen)\n")

    test_features = encoder.encode(TEST)
    preds = head.predict(test_features)
    probs = head.predict_proba(test_features)[:, 1]

    print("Predictions on unseen sentences:")
    for text, pred, prob in zip(TEST, preds, probs):
        label = "positive" if pred == 1 else "negative"
        print(f"  [{label:>8} p={prob:.2f}] {text!r}")

    print("\nTakeaway: a frozen base plus a tiny head learns a new task cheaply.")


if __name__ == "__main__":
    main()
