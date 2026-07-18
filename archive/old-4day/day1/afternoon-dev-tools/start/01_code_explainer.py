"""
Lab: Code Explainer
Goal: Build a tool that takes Python code and returns a plain-English explanation.

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
    }
]

def explain_code(code_snippet, name="Unknown"):
    """Send code to the LLM for explanation."""
    # TODO: Implement this function
    # 1. Create the messages array with SYSTEM_MESSAGE and the user's code
    # 2. Call get_completion (Hint: temperature=0.3 is good for explanations)
    # 3. Return the explanation text

    return "⚠️ TODO: Implement the explain_code function!"

def main():
    show_config()
    print("\n🔍 Code Explainer")
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
