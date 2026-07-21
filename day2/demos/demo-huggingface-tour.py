"""
Demo - A Short Hugging Face Tour
Day 2 - Session 2

Goal: Show how the transformers `pipeline` helper runs pre-trained models in a
few lines across several tasks.

We run three tasks with one high-level API: sentiment analysis (BERT-style
understanding), text generation (GPT-style generation), and fill-mask (an
encoder predicting a masked word). Each pipeline downloads a small model once,
then caches it.

Run: python3 day2/demos/demo-huggingface-tour.py
"""

from transformers import pipeline


def demo_sentiment():
    """Understanding task: classify the sentiment of a sentence."""
    print("\n1. Sentiment analysis (encoder-style understanding)")
    classifier = pipeline("sentiment-analysis")
    for text in ["I love this course!", "This bug ruined my afternoon."]:
        result = classifier(text)[0]
        print(f"  {text!r} -> {result['label']} ({result['score']:.2f})")


def demo_generation():
    """Generation task: continue a prompt with GPT-2."""
    print("\n2. Text generation (decoder-style generation)")
    generator = pipeline("text-generation", model="gpt2")
    out = generator(
        "In the future, software developers will",
        max_new_tokens=20,
        num_return_sequences=1,
        pad_token_id=50256,
    )
    print(f"  {out[0]['generated_text']!r}")


def demo_fill_mask():
    """Understanding task: BERT fills in a masked word using both directions."""
    print("\n3. Fill-mask (encoder predicting a masked word)")
    fill = pipeline("fill-mask", model="distilbert-base-uncased")
    for result in fill("The capital of France is [MASK].")[:3]:
        print(f"  {result['token_str']!r}  score = {result['score']:.3f}")


def main():
    print("Running three Hugging Face pipelines. Models download once, then cache.")
    demo_sentiment()
    demo_generation()
    demo_fill_mask()
    print("\nOne API, many tasks: pipeline handles tokenizing, running, and decoding.")


if __name__ == "__main__":
    main()
