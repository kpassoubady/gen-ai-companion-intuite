import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI()

# Option C: Bug-Report Triager
SYSTEM_PROMPT = """You are a bug report triager. For each bug report:
1. Classify severity: CRITICAL / HIGH / MEDIUM / LOW
2. Categorize: UI / API / Database / Security / Performance / Other
3. Suggest which team should handle it
4. Extract key symptoms

Respond in JSON format exactly like this:
{
    "severity": "...", 
    "category": "...", 
    "team": "...",
    "symptoms": ["..."], 
    "summary": "..."
}"""

def triage_bug(bug_report):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Bug Report:\n{bug_report}"}
            ],
            temperature=0.0
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"API Error: {e}")
        return {"error": str(e)}

def evaluate_triager(test_cases):
    results = []
    print("--- Running Evaluation ---")
    for test in test_cases:
        print(f"Evaluating: {test['report'][:50]}...")
        result = triage_bug(test['report'])
        
        # Simple evaluation: Did we get the expected severity and category?
        severity_match = result.get("severity") == test["expected_severity"]
        category_match = result.get("category") == test["expected_category"]
        
        results.append({
            "passed": severity_match and category_match,
            "expected": f"{test['expected_severity']} / {test['expected_category']}",
            "actual": f"{result.get('severity')} / {result.get('category')}"
        })
    
    passed_count = sum(1 for r in results if r["passed"])
    print(f"\nEvaluation Results: {passed_count}/{len(test_cases)} Passed")
    for i, r in enumerate(results):
        if not r["passed"]:
            print(f"Test {i+1} Failed: Expected {r['expected']}, got {r['actual']}")
    print("--- Evaluation Complete ---\n")

def main():
    test_cases = [
        {
            "report": "The login page crashes when I enter a password with a special character. I can't log in.",
            "expected_severity": "HIGH",
            "expected_category": "Security" # Or UI/API, could be subjective, but let's test how it does
        },
        {
            "report": "There is a typo on the about us page. It says 'teh' instead of 'the'.",
            "expected_severity": "LOW",
            "expected_category": "UI"
        },
        {
            "report": "The database queries are taking over 10 seconds to respond causing timeouts for everyone.",
            "expected_severity": "CRITICAL",
            "expected_category": "Database"
        }
    ]
    
    print("Testing Bug Triager (Option C)...\n")
    # Run evaluation
    evaluate_triager(test_cases)
    
    print("Interactive Mode:")
    while True:
        user_input = input("\nEnter a bug report (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        result = triage_bug(user_input)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
