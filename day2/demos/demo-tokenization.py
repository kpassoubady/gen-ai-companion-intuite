"""
Demo - Tokenization: BPE and WordPiece
Day 2 - Session 1

Goal: Show that models see text as a sequence of integer token IDs, and that
subword tokenization splits rare words into known pieces.

We tokenize the same sentences two ways: GPT-style BPE (tiktoken) and BERT-style
WordPiece (transformers). We print the tokens, the integer IDs, and the token
count so students can see why token count, not word count, is the real budget.

No API key needed. tiktoken runs offline; the BERT tokenizer downloads a small
vocab file once, then caches.

Run: python3 day2/demos/demo-tokenization.py
"""

import tiktoken
from transformers import AutoTokenizer

SENTENCES = [
    "The cat sat on the mat.",
    "Tokenization splits rare words into subwords.",
    "acetaminophen",
    "def get_weather(city): return api.fetch(city)",
]


def demo_bpe():
    """GPT-style Byte Pair Encoding with tiktoken (fully offline)."""
    print("\n1. BPE (GPT family, via tiktoken)")
    encoder = tiktoken.get_encoding("cl100k_base")
    for text in SENTENCES:
        ids = encoder.encode(text)
        pieces = [encoder.decode([i]) for i in ids]
        print(f"\n  text   : {text!r}")
        print(f"  tokens : {pieces}")
        print(f"  ids    : {ids}")
        print(f"  count  : {len(ids)} tokens for {len(text)} characters")


def demo_wordpiece():
    """BERT-style WordPiece with the transformers tokenizer."""
    print("\n\n2. WordPiece (BERT family, via transformers)")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    for text in SENTENCES:
        tokens = tokenizer.tokenize(text)
        ids = tokenizer.convert_tokens_to_ids(tokens)
        print(f"\n  text   : {text!r}")
        print(f"  tokens : {tokens}")
        print(f"  ids    : {ids}")
        print(f"  count  : {len(tokens)} tokens")
    print("\n  Note: '##' marks a piece that attaches to the previous token.")


def main():
    print("Same text, two tokenizers. Watch how rare words split into subwords.")
    demo_bpe()
    demo_wordpiece()
    print("\n\nTakeaway: models count tokens, not words. Rare words cost more tokens.")


if __name__ == "__main__":
    main()
