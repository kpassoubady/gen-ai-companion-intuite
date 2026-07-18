"""
Lab 2.3 — Temperature Experiment
Day 2 — Session 3

Goal: See how temperature affects output quality and creativity.

Instructions:
1. Run the same creative prompt at temperatures: 0.0, 0.2, 0.5, 0.7, 1.0, 1.2
2. Log all outputs side by side
3. Rate each set: creativity (1-5), relevance (1-5), coherence (1-5)
4. Find the "sweet spot" for this task
5. Bonus: Try the same experiment with top_p values

Run: python3 day2/labs/lab2_3_temperature.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from shared import get_completion_full, show_config


TEMPERATURES = [0.0, 0.2, 0.5, 0.7, 1.0, 1.2]

# Creative task prompt
SYSTEM_MESSAGE = (
    "You are a creative marketing copywriter specializing in tech brands. "
    "Be clever, punchy, and memorable."
)

CREATIVE_PROMPT = (
    "Generate 5 marketing taglines for a coffee shop called 'Byte Brew' "
    "that caters to software developers. Each tagline should be under "
    "10 words. Number them 1-5."
)

# Deterministic task prompt (for comparison)
DETERMINISTIC_SYSTEM = (
    "You are a Python code generator. Write clean, correct code. "
    "Include type hints and a docstring."
)

DETERMINISTIC_PROMPT = (
    "Write a Python function called 'flatten_dict' that takes a nested "
    "dictionary and returns a flat dictionary with dot-separated keys. "
    "Example: {'a': {'b': 1}} → {'a.b': 1}"
)


def run_temperature_experiment(system, prompt, task_name):
    """Run the same prompt at different temperatures and compare."""
    print(f"\n{'='*70}")
    print(f"Experiment: {task_name}")
    print(f"Prompt: {prompt[:80]}...")
    print(f"{'='*70}")

    results = []

    for temp in TEMPERATURES:

        # results.append({
        #     "temperature": temp,
        #     "content": content,
        #     "tokens": usage.completion_tokens,
        # })

        # print(f"\n--- Temperature: {temp} ---")
        # print(f"Tokens: {usage.completion_tokens}")
        # print(content)


    return results


def run_top_p_experiment(system, prompt, task_name):
    """Bonus: Run the same prompt at different top_p values."""
    top_p_values = [0.3, 0.5, 0.7, 0.9, 1.0]

    print(f"\n{'='*70}")
    print(f"Bonus Experiment: {task_name} (top_p)")
    print(f"{'='*70}")

    for top_p in top_p_values:

        print(f"\n--- top_p: {top_p} ---")


def main():
    show_config()
    print("\n🌡️  Temperature Experiment — Lab 2.3")

    # Experiment 1: Creative task
    run_temperature_experiment(
        SYSTEM_MESSAGE, CREATIVE_PROMPT, "Creative Taglines"
    )

    # Experiment 2: Deterministic task
    run_temperature_experiment(
        DETERMINISTIC_SYSTEM, DETERMINISTIC_PROMPT, "Code Generation"
    )

    # Bonus: top_p experiment
    run_top_p_experiment(
        SYSTEM_MESSAGE, CREATIVE_PROMPT, "Creative Taglines"
    )

    print(f"\n{'='*70}")
    print("📊 Your analysis:")
    print("   Rate each temperature setting for the creative task:")
    print("   - Creativity (1-5): How original are the taglines?")
    print("   - Relevance (1-5): Are they appropriate for a dev coffee shop?")
    print("   - Coherence (1-5): Do they make sense?")
    print(f"{'='*70}")

    print("\n✅ Lab 2.3 complete!")


if __name__ == "__main__":
    main()
