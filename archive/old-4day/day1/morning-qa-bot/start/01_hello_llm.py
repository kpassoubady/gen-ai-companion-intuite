"""
Lab: Hello LLM
Goal: Make 5 different API calls covering different NLP tasks.

Instructions:
Complete each of the 5 tasks below by calling the LLM API.
Run: cd to this directory, then execute 'python 01_hello_llm.py'
"""

import sys
sys.path.insert(0, "../../..") # To import shared

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
    show_config()
    print()

    # ------------------------------------------------------------------
    # Task 1: Summarization
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

    # TODO: Call get_completion_full with a system message and the user's paragraph
    # log_response("1. Summarization", paragraph, response)

    # ------------------------------------------------------------------
    # Task 2: Classification
    # ------------------------------------------------------------------
    review = "The special effects were stunning but the plot was predictable and the acting felt wooden."
    
    # TODO: Complete this task. Hint: Classify as POSITIVE, NEGATIVE, or NEUTRAL.

    # ------------------------------------------------------------------
    # Task 3: Translation
    # ------------------------------------------------------------------
    sentence = "The quick brown fox jumps over the lazy dog."

    # TODO: Translate to Spanish

    # ------------------------------------------------------------------
    # Task 4: Code Generation
    # ------------------------------------------------------------------
    
    # TODO: Generate a Python function to find the nth Fibonacci number.

    # ------------------------------------------------------------------
    # Task 5: Explain Like I'm 10
    # ------------------------------------------------------------------

    # TODO: Explain "recursion" to a 10-year-old.

    print("\n✅ Hello LLM complete!")

if __name__ == "__main__":
    main()
