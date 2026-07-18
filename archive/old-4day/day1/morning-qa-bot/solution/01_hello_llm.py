"""
Lab 1.1 — "Hello LLM"
Day 1 — Session 2

Goal: Make 5 different API calls covering different NLP tasks.
      Log each prompt, response, and token count.

Instructions:
1. Run show_config() to verify your setup
2. Complete each of the 5 tasks below
3. Try each with tier="mini" and tier="default" — compare quality
4. Bonus: Add your own 6th task

Run: cd to this directory, then execute 'python 01_hello_llm.py'
"""

import sys
sys.path.insert(0, "../../..")

from shared import get_completion_full, show_config


def log_response(task_name, prompt, response):
    """Helper to log a task's results."""
    content = response.choices[0].message.content
    usage = response.usage
    print(f"\n{'='*60}")
    print(f"Task: {task_name}")
    print(f"Prompt: {prompt[:100]}...")
    print(f"Tokens: {usage.prompt_tokens} in + {usage.completion_tokens} out")
    print(f"Response:\n{content}")
    print(f"{'='*60}")


def main():
    # Step 1: Verify environment
    print("Environment Check:")
    show_config()
    print()

    # ------------------------------------------------------------------
    # Task 1: Summarization
    # Summarize the following paragraph into 2 sentences.
    # ------------------------------------------------------------------
    paragraph = (
        "Machine learning is a subset of artificial intelligence that "
        "focuses on building systems that learn from data. Unlike "
        "traditional programming where rules are explicitly coded, ML "
        "algorithms identify patterns in data and make decisions with "
        "minimal human intervention. This approach has revolutionized "
        "fields from healthcare to finance, enabling applications like "
        "fraud detection, medical diagnosis, and recommendation systems."
    )

    response = get_completion_full(
        messages=[
            {"role": "system", "content": "Summarize in exactly 2 sentences."},
            {"role": "user", "content": paragraph},
        ],
        tier="mini",
    )
    log_response("1. Summarization", paragraph, response)

    # ------------------------------------------------------------------
    # Task 2: Classification
    # Classify the movie review as POSITIVE, NEGATIVE, or NEUTRAL.
    # ------------------------------------------------------------------
    review = "The special effects were stunning but the plot was predictable and the acting felt wooden."

    response = get_completion_full(
        messages=[
            {"role": "system", "content": "Classify as POSITIVE, NEGATIVE, or NEUTRAL. Respond with only the label."},
            {"role": "user", "content": review},
        ],
    )
    log_response("2. Classification", review, response)

    # ------------------------------------------------------------------
    # Task 3: Translation
    # Translate a sentence to Spanish.
    # ------------------------------------------------------------------
    sentence = "The quick brown fox jumps over the lazy dog."

    response = get_completion_full(
        messages=[
            {"role": "system", "content": "Translate the following sentence to Spanish."},
            {"role": "user", "content": sentence},
        ],
    )
    log_response("3. Translation", sentence, response)

    # ------------------------------------------------------------------
    # Task 4: Code Generation
    # Generate a Python function to find the nth Fibonacci number.
    # ------------------------------------------------------------------
    prompt4 = "Generate a Python function to find the nth Fibonacci number."
    response = get_completion_full(
        messages=[
            {"role": "user", "content": prompt4},
        ],
        temperature=0.0,
    )
    log_response("4. Code Generation", prompt4, response)

    # ------------------------------------------------------------------
    # Task 5: Explain Like I'm 10
    # Explain "recursion" to a 10-year-old.
    # ------------------------------------------------------------------
    prompt5 = "Explain recursion."
    response = get_completion_full(
        messages=[
            {"role": "system", "content": "Explain concepts as if you are talking to a 10-year-old."},
            {"role": "user", "content": prompt5},
        ],
    )
    log_response("5. Explain Like I'm 10", prompt5, response)

    print("\n✅ Lab 1.1 complete!")


if __name__ == "__main__":
    main()
