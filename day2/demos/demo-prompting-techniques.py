"""
Demo - Prompting Techniques on a Local Model
Day 2 - Session 3

Goal: Show zero-shot, few-shot, and chain-of-thought prompting without any API
key, using a small instruction-tuned model that runs on the laptop.

We use google/flan-t5-base, an instruction-following model, loaded directly with
transformers. The same techniques transfer directly to GPT, Claude, and Gemini;
only the client call changes. Decoding is greedy so the demo is repeatable.

No API key needed. The model downloads once (~1 GB), then caches. For a smaller
download set MODEL_NAME to "google/flan-t5-small".

Run: python3 day2/demos/demo-prompting-techniques.py
"""

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "google/flan-t5-base"


def make_generator(model, tokenizer):
    """Return a greedy text-in, text-out function backed by flan-t5."""
    def generate(prompt, max_new_tokens=64):
        inputs = tokenizer(prompt, return_tensors="pt")
        output_ids = model.generate(**inputs, max_new_tokens=max_new_tokens)
        return tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return generate


def run(generate, label, prompt):
    """Print a labeled prompt and the model's answer."""
    answer = generate(prompt).strip()
    print(f"\n{label}")
    print(f"  prompt : {prompt}")
    print(f"  answer : {answer}")


def demo_zero_shot(generate):
    print("\n1. Zero-shot (no examples, rely on what the model knows)")
    run(
        generate,
        "Sentiment classification",
        "Classify the sentiment as POSITIVE, NEGATIVE, or NEUTRAL. "
        "Text: The update completely broke my workflow.",
    )


def demo_few_shot(generate):
    print("\n\n2. Few-shot (a few examples teach the pattern and format)")
    run(
        generate,
        "Sentiment with examples",
        "Classify the sentiment.\n"
        "Text: Best purchase ever. -> POSITIVE\n"
        "Text: Broke after one day. -> NEGATIVE\n"
        "Text: The battery could be better but I like it. ->",
    )


def demo_chain_of_thought(generate):
    print("\n\n3. Chain-of-thought (ask for step-by-step reasoning)")
    run(
        generate,
        "Direct answer (small model slips on multi-step math)",
        "A week has 7 days. How many days are in 3 weeks?",
    )
    run(
        generate,
        "With 'think step by step'",
        "A week has 7 days. How many days are in 3 weeks? Think step by step.",
    )


def main():
    print(f"Loading {MODEL_NAME} (downloads once, then cached)...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    model.eval()
    generate = make_generator(model, tokenizer)

    demo_zero_shot(generate)
    demo_few_shot(generate)
    demo_chain_of_thought(generate)

    print("\n\nTakeaway: the technique lives in the prompt, not the provider.")
    print("The same zero/few-shot and CoT patterns work on any LLM API.")


if __name__ == "__main__":
    main()
