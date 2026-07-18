"""
Lab 2.1 — Sentiment Classifier: Zero-Shot to Few-Shot
Day 2 — Session 2

Goal: Build a sentiment classifier, first with zero-shot, then improve with few-shot.

Instructions:
1. Implement zero_shot_classify() — direct instruction, no examples
2. Test on the 10 sample texts, note where it fails
3. Implement few_shot_classify() — add 3-5 examples
4. Compare accuracy: zero-shot vs few-shot
5. Bonus: Add a confidence score to the output

Run: python3 day2/labs/lab2_1_sentiment.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from shared import get_completion, show_config


# Test data — 10 texts with expected sentiments
TEST_DATA = [
    {"text": "This product is absolutely amazing! Best purchase I've ever made.",
     "expected": "POSITIVE"},
    {"text": "Terrible experience. The item broke after one day of use.",
     "expected": "NEGATIVE"},
    {"text": "It works as described. Nothing special, nothing bad.",
     "expected": "NEUTRAL"},
    {"text": "The battery life could be better, but overall I really like it.",
     "expected": "POSITIVE"},
    {"text": "I've been waiting 3 weeks and still no delivery. Very frustrated.",
     "expected": "NEGATIVE"},
    {"text": "It's a product. It does what it says. Fine I guess.",
     "expected": "NEUTRAL"},
    {"text": "Wow, exceeded all my expectations! The quality is outstanding.",
     "expected": "POSITIVE"},
    {"text": "Not worth the price. There are much better alternatives.",
     "expected": "NEGATIVE"},
    {"text": "Received the package on time. Standard packaging.",
     "expected": "NEUTRAL"},
    {"text": "The design is gorgeous but the software is buggy and slow.",
     "expected": "NEGATIVE"},
]


def zero_shot_classify(text):
    """Classify sentiment using zero-shot prompting (no examples)."""
    # TODO: Implement zero-shot classification
    # 1. Create a system message that instructs classification
    # 2. Send the text as the user message
    # 3. Return the label: POSITIVE, NEGATIVE, or NEUTRAL

    return "TODO"


def few_shot_classify(text):
    """Classify sentiment using few-shot prompting (with examples)."""
    # TODO: Implement few-shot classification
    # 1. Create messages with system prompt + example pairs
    # 2. Add 3-5 user/assistant message pairs as examples
    # 3. Add the actual text to classify as the final user message
    # 4. Return the label

    return "TODO"


def evaluate(classify_fn, label):
    """Run a classifier against the test data and report accuracy."""
    correct = 0
    results = []

    for item in TEST_DATA:
        prediction = classify_fn(item["text"])
        is_correct = prediction == item["expected"]
        if is_correct:
            correct += 1

        results.append({
            "text": item["text"][:60] + "...",
            "expected": item["expected"],
            "predicted": prediction,
            "correct": "✅" if is_correct else "❌",
        })

    accuracy = correct / len(TEST_DATA) * 100

    print(f"\n{'='*70}")
    print(f"Results: {label}")
    print(f"{'='*70}")
    for r in results:
        print(f"  {r['correct']} Expected: {r['expected']:8} | "
              f"Got: {r['predicted']:8} | {r['text']}")
    print(f"\nAccuracy: {correct}/{len(TEST_DATA)} ({accuracy:.0f}%)")
    print(f"{'='*70}")

    return accuracy


def main():
    show_config()
    print("\n🎯 Sentiment Classifier — Lab 2.1")

    # Step 1: Zero-shot classification
    print("\n--- Zero-Shot Classification ---")
    zero_accuracy = evaluate(zero_shot_classify, "Zero-Shot")

    # Step 2: Few-shot classification
    print("\n--- Few-Shot Classification ---")
    few_accuracy = evaluate(few_shot_classify, "Few-Shot")

    # Step 3: Compare
    print(f"\n📊 Comparison:")
    print(f"   Zero-shot: {zero_accuracy:.0f}%")
    print(f"   Few-shot:  {few_accuracy:.0f}%")
    print(f"   Improvement: {few_accuracy - zero_accuracy:+.0f}%")

    print("\n✅ Lab 2.1 complete!")


if __name__ == "__main__":
    main()
