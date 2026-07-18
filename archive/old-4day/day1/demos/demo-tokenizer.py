"""
Demo: Tokenizer Visualization with tiktoken
Day 1 — Session 1

Run: python3 day1/demos/demo-tokenizer.py
"""

import tiktoken


def demo_model_comparison():
    """Compare tokenizers across different models."""
    print("=" * 60)
    print("1. Tokenizer Comparison Across Models")
    print("=" * 60)

    text = "Generative AI is transforming software development."

    for model in ["gpt-4o", "gpt-4o-mini", "gpt-4"]:
        enc = tiktoken.encoding_for_model(model)
        tokens = enc.encode(text)
        print(f"\n  {model:15} → {len(tokens)} tokens")
        print(f"  Token IDs: {tokens}")
        # Show each token as text
        for t in tokens:
            print(f"    {t:8} → '{enc.decode([t])}'")


def demo_language_comparison():
    """Show how different languages tokenize differently."""
    print("\n" + "=" * 60)
    print("2. Tokenization Across Languages")
    print("=" * 60)

    texts = [
        ("English", "Hello, world!"),
        ("French", "Bonjour le monde!"),
        ("Japanese", "こんにちは世界！"),
        ("Chinese", "你好世界！"),
        ("Python", "def hello(): return 'world'"),
        ("JSON", '{"name": "Alice", "age": 30}'),
    ]

    enc = tiktoken.encoding_for_model("gpt-4o")
    for label, text in texts:
        tokens = enc.encode(text)
        print(f"\n  {label:10} ({len(tokens):2} tokens): {text}")
        print(f"  Token IDs: {tokens}")


def demo_token_cost():
    """Estimate costs for different text sizes."""
    print("\n" + "=" * 60)
    print("3. Token Counting & Cost Estimation")
    print("=" * 60)

    enc = tiktoken.encoding_for_model("gpt-4o")

    samples = [
        ("Short prompt", "Explain recursion in one sentence."),
        ("Medium prompt", "You are a senior Python developer. Explain the "
         "difference between a list and a tuple in Python. Include code "
         "examples and performance considerations."),
        ("Long prompt", open(__file__).read()),  # This script itself!
    ]

    # Pricing per 1M tokens
    pricing = {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    }

    for label, text in samples:
        token_count = len(enc.encode(text))
        print(f"\n  {label}: {token_count} tokens ({len(text)} chars)")
        for model, prices in pricing.items():
            cost = token_count * prices["input"] / 1_000_000
            print(f"    {model:15} input cost: ${cost:.6f}")


def demo_special_tokens():
    """Show interesting tokenization edge cases."""
    print("\n" + "=" * 60)
    print("4. Interesting Edge Cases")
    print("=" * 60)

    enc = tiktoken.encoding_for_model("gpt-4o")

    edge_cases = [
        "Hello",
        " Hello",          # Leading space changes tokenization
        "hello",           # Case matters
        "HELLO",
        "Hello!!!",
        "Hello   world",   # Multiple spaces
        "indivisibility",  # Long words get split
        "🚀🤖✨",          # Emojis
    ]

    for text in edge_cases:
        tokens = enc.encode(text)
        decoded = [enc.decode([t]) for t in tokens]
        print(f"\n  '{text}' → {len(tokens)} tokens: {decoded}")


if __name__ == "__main__":
    demo_model_comparison()
    demo_language_comparison()
    demo_token_cost()
    demo_special_tokens()
    print("\n" + "=" * 60)
    print("Demo complete!")
    print("=" * 60)
