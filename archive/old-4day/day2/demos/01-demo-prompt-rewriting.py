"""
Demo: Rewriting a Bad Prompt — 5 Iterations Live
Day 2 — Session 1

Shows how iterating on a prompt dramatically improves output quality.
Each version builds on the previous one.

Run: python3 day2/demos/demo-prompt-rewriting.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from shared import get_completion_full, show_config


# The 5 prompt iterations — each one better than the last
ITERATIONS = [
    {
        "version": "v0 — Original (vague)",
        "system": "You are a helpful assistant.",
        "user": "Tell me about Python errors",
        "change": "Baseline: vague, no specificity, no format",
    },
    {
        "version": "v1 — Add specificity",
        "system": "You are a helpful assistant.",
        "user": "Explain the 5 most common Python errors that beginners encounter.",
        "change": "Added: specific number (5), specific audience (beginners), specific ask (most common)",
    },
    {
        "version": "v2 — Add context",
        "system": "You are a patient Python tutor teaching a bootcamp for career changers with no prior programming experience.",
        "user": "Explain the 5 most common Python errors that beginners encounter.",
        "change": "Added: role/persona, audience context (career changers, no experience)",
    },
    {
        "version": "v3 — Add output format",
        "system": "You are a patient Python tutor teaching a bootcamp for career changers with no prior programming experience.",
        "user": (
            "Explain the 5 most common Python errors that beginners encounter.\n\n"
            "Format as a table with columns: Error Name | What It Means | Example Code | How to Fix"
        ),
        "change": "Added: specific output format (table with defined columns)",
    },
    {
        "version": "v4 — Add constraints",
        "system": "You are a patient Python tutor teaching a bootcamp for career changers with no prior programming experience.",
        "user": (
            "Explain the 5 most common Python errors that beginners encounter.\n\n"
            "Format as a table with columns: Error Name | What It Means | Example Code | How to Fix\n\n"
            "Rules:\n"
            "- Each cell should be one sentence maximum\n"
            "- Example code should be a single line\n"
            "- Use simple, jargon-free language\n"
            "- Order by frequency (most common first)"
        ),
        "change": "Added: constraints (length, simplicity, ordering)",
    },
    {
        "version": "v5 — Add an example (few-shot)",
        "system": "You are a patient Python tutor teaching a bootcamp for career changers with no prior programming experience.",
        "user": (
            "Explain the 5 most common Python errors that beginners encounter.\n\n"
            "Format as a table with columns: Error Name | What It Means | Example Code | How to Fix\n\n"
            "Rules:\n"
            "- Each cell should be one sentence maximum\n"
            "- Example code should be a single line\n"
            "- Use simple, jargon-free language\n"
            "- Order by frequency (most common first)\n\n"
            "Example row:\n"
            "| SyntaxError | You typed something Python can't understand. "
            "| `print('hello'` | Check for missing parentheses, quotes, or colons. |"
        ),
        "change": "Added: one example row showing the exact format and level of detail expected",
    },
]


def run_demo():
    """Run each iteration and show the progression."""
    show_config()
    print("\n🔄 Demo: Prompt Rewriting — 5 Iterations")
    print("Watch how small changes dramatically improve output quality.\n")

    for i, iteration in enumerate(ITERATIONS):
        print(f"\n{'='*70}")
        print(f"📌 {iteration['version']}")
        print(f"   Change: {iteration['change']}")
        print(f"{'='*70}")
        print(f"\nSystem: {iteration['system'][:80]}...")
        print(f"User:   {iteration['user'][:80]}...")
        print(f"{'─'*70}")

        try:
            response = get_completion_full(
                messages=[
                    {"role": "system", "content": iteration["system"]},
                    {"role": "user", "content": iteration["user"]},
                ],
                temperature=0.3,
                max_tokens=800,
            )

            content = response.choices[0].message.content
            usage = response.usage

            print(f"Tokens: {usage.prompt_tokens} in + "
                  f"{usage.completion_tokens} out = "
                  f"{usage.total_tokens} total")
            print(f"\nOutput:\n{content}")

        except Exception as e:
            print(f"Error: {e}")

        # Pause between iterations for live demo
        if i < len(ITERATIONS) - 1:
            input(f"\n⏎  Press Enter for the next iteration...")

    print(f"\n{'='*70}")
    print("📊 Summary of improvements:")
    print("   v0 → v1: Specificity eliminates vague, unfocused output")
    print("   v1 → v2: Context/role shapes tone and detail level")
    print("   v2 → v3: Format makes output scannable and consistent")
    print("   v3 → v4: Constraints keep output concise and ordered")
    print("   v4 → v5: Example teaches the exact pattern expected")
    print(f"{'='*70}")
    print("\n✅ Demo complete!")


if __name__ == "__main__":
    run_demo()
