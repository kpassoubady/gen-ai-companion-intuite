"""
Lab 1.3 — Code Explainer
Day 1 — Session 4

Goal: Build a tool that takes Python code and returns a plain-English explanation.

Requirements:
1. Accept a Python code snippet (hardcoded samples or from file)
2. Use a system message for senior developer persona
3. Output: function purpose, parameters, return value, logic, complexity
4. Format the explanation in Markdown

Run: cd to this directory, then execute 'python 01_code_explainer.py'
"""

import sys
sys.path.insert(0, "../../..")

from shared import get_completion, show_config

SYSTEM_MESSAGE = """You are a senior Python developer explaining code to a junior colleague.

For each function provided, explain:
1. **Purpose**: What does this function do? (one sentence)
2. **Parameters**: List each parameter and its expected type/purpose
3. **Return value**: What does it return?
4. **Algorithm**: Step-by-step explanation of the logic
5. **Complexity**: Time and space complexity (Big O)
6. **Edge cases**: What inputs might cause issues?

Use Markdown formatting. Be clear and concise."""

# Sample code snippets to explain
SAMPLES = [
    {
        "name": "Binary Search",
        "code": '''
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
''',
    },
    {
        "name": "Memoized Fibonacci",
        "code": '''
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
''',
    },
    {
        "name": "Flatten Nested List",
        "code": '''
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
''',
    },
]


def explain_code(code_snippet, name="Unknown"):
    """Send code to the LLM for explanation."""
    response = get_completion(
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": f"Explain this code:\n\n```python\n{code_snippet}\n```"},
        ],
        temperature=0.3,
    )
    return response


def main():
    show_config()
    print("\n🔍 Code Explainer — Lab 1.3")
    print("=" * 60)

    for sample in SAMPLES:
        print(f"\n📝 Explaining: {sample['name']}")
        print(f"{'─'*40}")
        print(f"Code:\n{sample['code']}")
        print(f"{'─'*40}")

        explanation = explain_code(sample["code"], sample["name"])
        print(f"Explanation:\n{explanation}")
        print(f"{'='*60}")


if __name__ == "__main__":
    main()
