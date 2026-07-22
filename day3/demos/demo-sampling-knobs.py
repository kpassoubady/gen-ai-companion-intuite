"""
Demo - Sampling Knobs in Text Generation
Day 3 - Session 2

Goal: Show how temperature, top-k, top-p, and beam search change generated text.

We load a small GPT-2 model and generate from one prompt under several decoding
settings, printing each result so the effect of every knob is visible. Greedy and
low temperature stay repetitive and safe; higher temperature and sampling add
variety; beam search favors fluent, high-probability text.

Run: python3 day3/demos/demo-sampling-knobs.py
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed

MODEL_NAME = "gpt2"
PROMPT = "The best way to learn programming is"
NEW_TOKENS = 30


def generate(model, tokenizer, label, **kwargs):
    """Generate one continuation of the prompt and print it under a label."""
    set_seed(42)
    inputs = tokenizer(PROMPT, return_tensors="pt")
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=NEW_TOKENS,
            pad_token_id=tokenizer.eos_token_id,
            **kwargs,
        )
    text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    print(f"\n[{label}]")
    print(f"  {text}")


def main():
    print(f"Loading {MODEL_NAME} (downloads once, then cached)...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    model.eval()

    print(f"\nPrompt: {PROMPT!r}")

    generate(model, tokenizer, "greedy (do_sample=False)", do_sample=False)
    generate(model, tokenizer, "temperature=0.2 (focused)",
             do_sample=True, temperature=0.2)
    generate(model, tokenizer, "temperature=1.2 (wild)",
             do_sample=True, temperature=1.2)
    generate(model, tokenizer, "top_k=10", do_sample=True, top_k=10)
    generate(model, tokenizer, "top_p=0.90 (nucleus)",
             do_sample=True, top_p=0.90)
    generate(model, tokenizer, "beam search (num_beams=5)",
             do_sample=False, num_beams=5, early_stopping=True)

    print("\nSame prompt, different knobs, different text. That is decoding.")


if __name__ == "__main__":
    main()
