"""
Lab 4.3 — Evaluation Harness
Day 4 — Session 3

Goal: Build a script that runs test prompts, compares outputs to expected
results, and logs pass/fail.

Requirements:
1. Define 10 test cases with expected keywords and forbidden terms
2. Run each test case through the LLM
3. Score each response (keyword matching)
4. Log results with pass/fail status
5. Print a summary: total pass rate, worst performers, average score

Stretch goals:
- Add LLM-as-judge scoring alongside keyword scoring
- Compare results across two models (mini vs default)
- Save results to a JSON file for tracking over time

Run: python3 lab4_3_eval_harness.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import json
import time
from datetime import datetime
from shared import get_completion, show_config


# ---------------------------------------------------------------------------
# Golden dataset: 10 test cases
# ---------------------------------------------------------------------------
GOLDEN_DATASET = [
    {
        "id": "TC01",
        "input": "What is a Python list?",
        "expected_keywords": ["ordered", "mutable", "collection", "index"],
        "expected_not": ["immutable", "key-value"],
        "category": "data-structures",
    },
    {
        "id": "TC02",
        "input": "What is a Python dictionary?",
        "expected_keywords": ["key-value", "mutable", "hash"],
        "expected_not": ["ordered sequence", "linked list"],
        "category": "data-structures",
    },
    {
        "id": "TC03",
        "input": "How do I handle exceptions in Python?",
        "expected_keywords": ["try", "except"],
        "expected_not": ["JavaScript", "catch block"],
        "category": "error-handling",
    },
    {
        "id": "TC04",
        "input": "What is a Python decorator?",
        "expected_keywords": ["function", "wrapper", "@"],
        "expected_not": ["HTML", "CSS"],
        "category": "functions",
    },
    {
        "id": "TC05",
        "input": "Explain list comprehension in Python.",
        "expected_keywords": ["list", "expression", "for"],
        "expected_not": ["Java", "C++"],
        "category": "data-structures",
    },
    {
        "id": "TC06",
        "input": "What is the difference between a tuple and a list?",
        "expected_keywords": ["immutable", "mutable"],
        "expected_not": ["dictionary", "set"],
        "category": "data-structures",
    },
    {
        "id": "TC07",
        "input": "How do I read a file in Python?",
        "expected_keywords": ["open", "read"],
        "expected_not": ["JavaScript", "Node.js"],
        "category": "file-io",
    },
    {
        "id": "TC08",
        "input": "What is a virtual environment in Python?",
        "expected_keywords": ["isolated", "dependencies", "packages"],
        "expected_not": ["Docker", "container"],
        "category": "tooling",
    },
    {
        "id": "TC09",
        "input": "How do I install packages with pip?",
        "expected_keywords": ["pip", "install"],
        "expected_not": ["npm", "yarn"],
        "category": "tooling",
    },
    {
        "id": "TC10",
        "input": "What are Python f-strings?",
        "expected_keywords": ["format", "string", "expression"],
        "expected_not": ["Java", "printf"],
        "category": "strings",
    },
]


# ---------------------------------------------------------------------------
# Evaluation functions
# ---------------------------------------------------------------------------
def evaluate_response(response, test_case):
    """Score a response against expected criteria."""
    # TODO: Implement evaluation logic
    # 1. Check each expected keyword is present in the response
    # 2. Check each forbidden term is absent from the response
    # 3. Calculate a score (passed checks / total checks)
    # 4. Return dict with score, passed status, and details

    # Hint:
    # lower = response.lower()
    # passed_checks = 0
    # total_checks = 0
    # details = []
    #
    # for keyword in test_case["expected_keywords"]:
    #     total_checks += 1
    #     if keyword.lower() in lower:
    #         passed_checks += 1
    #         details.append(f"  ✅ Found: '{keyword}'")
    #     else:
    #         details.append(f"  ❌ Missing: '{keyword}'")
    #
    # for term in test_case.get("expected_not", []):
    #     total_checks += 1
    #     if term.lower() not in lower:
    #         passed_checks += 1
    #         details.append(f"  ✅ Absent: '{term}'")
    #     else:
    #         details.append(f"  ❌ Present (should be absent): '{term}'")
    #
    # score = passed_checks / total_checks if total_checks > 0 else 0
    # return {
    #     "score": score,
    #     "passed": passed_checks == total_checks,
    #     "checks": f"{passed_checks}/{total_checks}",
    #     "details": details,
    # }

    return {"score": 0, "passed": False, "checks": "0/0", "details": []}


def llm_as_judge(question, response):
    """Use an LLM to judge the quality of a response (Stretch goal)."""
    # TODO (Stretch): Implement LLM-as-judge scoring
    # 1. Create a judge prompt that asks the LLM to rate 1-5
    # 2. Parse the JSON response for score and reasoning
    # 3. Return the judgment

    # Hint:
    # judge_prompt = f"""Rate the following response on a scale of 1-5.
    #
    # Question: {question}
    # Response: {response}
    #
    # Criteria:
    # - Accuracy: Is the information correct?
    # - Completeness: Does it cover the key points?
    # - Clarity: Is it easy to understand?
    # - Conciseness: Is it appropriately brief?
    #
    # Respond with ONLY a JSON object:
    # {{"score": <1-5>, "reasoning": "<brief explanation>"}}"""
    #
    # try:
    #     judgment = get_completion(
    #         [{"role": "user", "content": judge_prompt}],
    #         temperature=0.0, tier="mini",
    #     )
    #     return json.loads(judgment)
    # except (json.JSONDecodeError, Exception) as e:
    #     return {"score": 0, "reasoning": f"Judge error: {e}"}

    return None  # TODO: replace (return None to skip)


# ---------------------------------------------------------------------------
# Test runner
# ---------------------------------------------------------------------------
SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a Python expert. Answer programming questions accurately "
        "and concisely. Keep responses under 100 words."
    ),
}


def run_evaluation(dataset, model_tier="mini"):
    """Run the full evaluation suite."""
    results = []
    total_score = 0
    total_passed = 0

    print(f"\n🧪 Running {len(dataset)} test cases (tier: {model_tier})...\n")
    print("-" * 60)

    for test_case in dataset:
        tc_id = test_case["id"]
        question = test_case["input"]

        # Get LLM response
        start_time = time.time()
        try:
            response = get_completion(
                [SYSTEM_MESSAGE,
                 {"role": "user", "content": question}],
                temperature=0.0,
                tier=model_tier,
            )
            latency_ms = (time.time() - start_time) * 1000
        except Exception as e:
            print(f"❌ {tc_id}: API error — {e}")
            results.append({
                "id": tc_id, "passed": False, "score": 0,
                "error": str(e),
            })
            continue

        # Evaluate
        eval_result = evaluate_response(response, test_case)

        # Optional: LLM-as-judge
        judge_result = llm_as_judge(question, response)

        # Display result
        status = "✅ PASS" if eval_result["passed"] else "❌ FAIL"
        print(f"{status} | {tc_id} | Score: {eval_result['score']:.0%} "
              f"({eval_result['checks']}) | {latency_ms:.0f}ms")
        print(f"   Q: {question}")
        print(f"   A: {response[:120]}{'...' if len(response) > 120 else ''}")

        if judge_result:
            print(f"   🧑‍⚖️ Judge: {judge_result.get('score', 'N/A')}/5 — "
                  f"{judge_result.get('reasoning', 'N/A')[:80]}")

        for detail in eval_result["details"]:
            print(f"   {detail}")
        print()

        # Track results
        total_score += eval_result["score"]
        if eval_result["passed"]:
            total_passed += 1

        results.append({
            "id": tc_id,
            "question": question,
            "response": response,
            "passed": eval_result["passed"],
            "score": eval_result["score"],
            "checks": eval_result["checks"],
            "latency_ms": latency_ms,
            "judge": judge_result,
            "category": test_case.get("category", "general"),
        })

    return results, total_score, total_passed


def print_summary(results, total_score, total_passed, total_tests):
    """Print evaluation summary."""
    print("=" * 60)
    print("📊 Evaluation Summary")
    print("=" * 60)

    pass_rate = total_passed / total_tests * 100 if total_tests > 0 else 0
    avg_score = total_score / total_tests if total_tests > 0 else 0

    print(f"\n   Total tests:  {total_tests}")
    print(f"   Passed:       {total_passed}")
    print(f"   Failed:       {total_tests - total_passed}")
    print(f"   Pass rate:    {pass_rate:.1f}%")
    print(f"   Avg score:    {avg_score:.0%}")

    # Worst performers
    failed = [r for r in results if not r["passed"]]
    if failed:
        print(f"\n   ❌ Failed test cases:")
        for r in failed:
            print(f"      {r['id']}: {r['question'][:50]}... "
                  f"(score: {r['score']:.0%})")

    # Category breakdown
    categories = {}
    for r in results:
        cat = r.get("category", "general")
        if cat not in categories:
            categories[cat] = {"passed": 0, "total": 0}
        categories[cat]["total"] += 1
        if r["passed"]:
            categories[cat]["passed"] += 1

    print(f"\n   📂 By category:")
    for cat, stats in sorted(categories.items()):
        rate = stats["passed"] / stats["total"] * 100
        print(f"      {cat}: {stats['passed']}/{stats['total']} "
              f"({rate:.0f}%)")

    print("=" * 60)


def save_results(results, filename="eval_results.json"):
    """Save results to JSON for tracking over time."""
    # TODO (Stretch): Save results to file
    # Hint:
    # output = {
    #     "timestamp": datetime.now().isoformat(),
    #     "total_tests": len(results),
    #     "passed": sum(1 for r in results if r["passed"]),
    #     "results": results,
    # }
    # with open(filename, "w") as f:
    #     json.dump(output, f, indent=2)
    # print(f"\n💾 Results saved to {filename}")

    pass  # TODO: replace


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    show_config()
    print("\n🧪 Evaluation Harness — Lab 4.3")

    results, total_score, total_passed = run_evaluation(GOLDEN_DATASET)
    print_summary(results, total_score, total_passed, len(GOLDEN_DATASET))

    # Optional: save results
    save_results(results)

    print("\n✅ Lab 4.3 complete!")


if __name__ == "__main__":
    main()
