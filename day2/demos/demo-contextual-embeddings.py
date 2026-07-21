"""
Demo - Contextual Embeddings with BERT
Day 2 - Session 2

Goal: Show that a Transformer encoder gives the same word different vectors
depending on context, which is what makes BERT more than a lookup table.

We run the word "bank" in three sentences (river bank, money bank, money bank)
through BERT and pull the hidden vector for that exact token in each sentence.
Cosine similarity is high for the two money sentences and lower for the river
sentence, so students see meaning shaped by surrounding words.

No API key needed. The BERT model downloads once (~420 MB), then caches.

Run: python3 day2/demos/demo-contextual-embeddings.py
"""

import numpy as np
import torch
from transformers import AutoModel, AutoTokenizer

MODEL_NAME = "bert-base-uncased"
SENTENCES = [
    "I sat by the river bank watching the water.",
    "I deposited my paycheck at the bank downtown.",
    "The bank approved my loan application today.",
]
TARGET_WORD = "bank"


def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def embed_target_word(model, tokenizer, sentence, word):
    """Return BERT's contextual vector for `word` inside `sentence`."""
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        hidden = model(**inputs).last_hidden_state[0]
    token_ids = inputs["input_ids"][0]
    word_id = tokenizer.convert_tokens_to_ids(word)
    positions = (token_ids == word_id).nonzero(as_tuple=True)[0]
    return hidden[positions[0]].numpy()


def main():
    print(f"Loading {MODEL_NAME} (downloads once, then cached)...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME)
    model.eval()

    vectors = [embed_target_word(model, tokenizer, s, TARGET_WORD) for s in SENTENCES]

    print(f"\nContextual vectors for the word {TARGET_WORD!r} in each sentence:")
    for i, s in enumerate(SENTENCES):
        print(f"  [{i}] {s}")

    print("\nCosine similarity between the 'bank' vectors:")
    print(f"  [0] river  vs [1] money  -> {cosine(vectors[0], vectors[1]):.2f}")
    print(f"  [1] money  vs [2] money  -> {cosine(vectors[1], vectors[2]):.2f}")
    print(f"  [0] river  vs [2] money  -> {cosine(vectors[0], vectors[2]):.2f}")

    print("\nTakeaway: same word, different vectors. Context changes meaning,")
    print("which a static bag-of-words or word2vec lookup cannot capture.")


if __name__ == "__main__":
    main()
