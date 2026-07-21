"""
Demo - GPT as an Autoregressive Model
Day 2 - Session 2

Goal: Show that generation is repeated next-token prediction.

We load a small GPT-2 model, print the top candidate next tokens with their
probabilities for a prompt, then generate a few tokens and watch the text grow
one token at a time. This is the whole idea behind text generation.

Run: python3 day2/demos/demo-autoregressive.py
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "gpt2"
PROMPT = "The cat sat on the"
TOP_K = 5
NEW_TOKENS = 8


def show_top_next_tokens(model, tokenizer, prompt, top_k=TOP_K):
    """Print the most likely next tokens for a prompt with their probabilities."""
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    next_token_logits = logits[0, -1, :]
    probs = torch.softmax(next_token_logits, dim=-1)
    top = torch.topk(probs, top_k)

    print(f"\nPrompt: {prompt!r}")
    print(f"Top {top_k} candidate next tokens:")
    for prob, token_id in zip(top.values, top.indices):
        token = tokenizer.decode(token_id)
        print(f"  {token!r:>12}  p = {prob.item():.3f}")


def generate_step_by_step(model, tokenizer, prompt, new_tokens=NEW_TOKENS):
    """Greedily add one token at a time and print the growing text."""
    print("\nGenerating one token at a time (greedy):")
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    for _ in range(new_tokens):
        with torch.no_grad():
            logits = model(input_ids).logits
        next_id = logits[0, -1, :].argmax().unsqueeze(0).unsqueeze(0)
        input_ids = torch.cat([input_ids, next_id], dim=1)
        print(f"  {tokenizer.decode(input_ids[0])!r}")


def main():
    print(f"Loading {MODEL_NAME} (downloads once, then cached)...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    model.eval()

    show_top_next_tokens(model, tokenizer, PROMPT)
    generate_step_by_step(model, tokenizer, PROMPT)

    print("\nGeneration is just this loop: predict, pick, append, repeat.")


if __name__ == "__main__":
    main()
