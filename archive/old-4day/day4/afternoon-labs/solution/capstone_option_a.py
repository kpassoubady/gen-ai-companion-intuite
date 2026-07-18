import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI()

# Simple mock for RAG (Retrieval-Augmented Generation)
CODING_STANDARDS = """
1. All functions must have docstrings.
2. Use snake_case for variable names.
3. Handle exceptions gracefully using try/except blocks.
4. Avoid hardcoding magic numbers; use constants.
"""

SYSTEM_PROMPT = f"""You are a code reviewer. Review the provided code against these standards retrieved from the team's coding guide:
{CODING_STANDARDS}

For each issue found:
1. Quote the problematic line
2. Explain why it's a problem
3. Suggest a fix

Rate the overall code quality at the very end: PASS / NEEDS_CHANGES / FAIL"""

def review_code(code):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Code to review:\n{code}"}
            ],
            temperature=0.0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"API Error: {e}"

def evaluate_assistant():
    test_cases = [
        {
            "name": "Good Code",
            "code": "def calculate_sum(a, b):\n    \"\"\"Calculates sum\"\"\"\n    return a + b",
            "expected_rating": "PASS"
        },
        {
            "name": "Missing Docstring & Bad Naming",
            "code": "def Calc(A, B):\n    return A + B",
            "expected_rating": "NEEDS_CHANGES"
        }
    ]
    
    print("--- Running Evaluation ---")
    for test in test_cases:
        print(f"\nEvaluating: {test['name']}")
        result = review_code(test['code'])
        # Simple evaluation: check if the expected rating is in the result
        passed = test['expected_rating'] in result
        print(f"Passed: {passed}")
    print("--- Evaluation Complete ---\n")

def main():
    print("Code Review Assistant (Option A)")
    
    # Run evaluation first
    evaluate_assistant()
    
    print("Interactive Mode:")
    print("Paste your Python code below (type 'END' on a new line to submit, or 'quit' to exit):")
    
    while True:
        code_lines = []
        while True:
            line = input()
            if line.strip().lower() == 'quit':
                return
            if line == 'END':
                break
            code_lines.append(line)
            
        code_to_review = "\n".join(code_lines)
        if code_to_review.strip():
            print("\nReviewing code...\n")
            print(review_code(code_to_review))
            print("\nPaste more code or type 'quit' to exit:")

if __name__ == "__main__":
    main()
