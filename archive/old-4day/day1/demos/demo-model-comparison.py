"""
Demo: Same Prompt, Different Models — Compare quality and cost.
Day 1 — Session 3

Run: python3 day1/demos/demo-model-comparison.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from shared import get_completion_full, get_model, show_config


def compare_models():
    """Send the same prompt to default and mini models, compare results."""
    show_config()
    print()

    prompt = (
        "Explain the CAP theorem to a junior developer. "
        "Include a real-world example with a specific technology "
        "(e.g., a database). Keep it under 200 words."
    )

    print(f"Prompt: {prompt}")
    print("=" * 60)

    for tier in ["mini", "default"]:
        model = get_model(tier)
        print(f"\n{'='*60}")
        print(f"Model: {model} (tier={tier})")
        print(f"{'='*60}")

        try:
            response = get_completion_full(
                messages=[{"role": "user", "content": prompt}],
                tier=tier,
                temperature=0.3,
            )

            content = response.choices[0].message.content
            usage = response.usage

            print(f"Tokens: {usage.prompt_tokens} in + "
                  f"{usage.completion_tokens} out = "
                  f"{usage.total_tokens} total")
            print(f"Finish reason: {response.choices[0].finish_reason}")
            print(f"\nResponse:\n{content}")

        except Exception as e:
            print(f"Error: {e}")

    print(f"\n{'='*60}")
    print("Compare: depth of explanation, examples, token usage.")
    print(f"{'='*60}")


if __name__ == "__main__":
    compare_models()
