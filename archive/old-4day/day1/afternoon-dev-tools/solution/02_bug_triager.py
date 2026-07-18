"""
Lab 1.4 — Bug Triager
Day 1 — Session 4

Goal: Build a tool that classifies error logs by severity and suggests fixes.

Requirements:
1. Accept an error log or stack trace as input
2. Classify severity: CRITICAL / HIGH / MEDIUM / LOW
3. Identify root cause
4. Suggest a fix
5. Output structured JSON

Run: cd to this directory, then execute 'python 02_bug_triager.py'
"""

import sys
import json

sys.path.insert(0, "../../..")

from shared import get_completion, show_config

SYSTEM_MESSAGE = """You are an expert software engineer specializing in debugging and incident response.

Given an error log or stack trace, analyze it and respond with ONLY valid JSON (no markdown, no explanation outside JSON):

{
  "severity": "CRITICAL | HIGH | MEDIUM | LOW",
  "category": "category of the error",
  "root_cause": "brief explanation of what caused this error",
  "affected_component": "which part of the code is affected",
  "suggested_fix": ["list", "of", "suggested", "fixes"],
  "immediate_action": "what to do right now"
}

Severity guidelines:
- CRITICAL: Data loss, security breach, complete system failure
- HIGH: Service outage, payment failures, blocking errors
- MEDIUM: Degraded performance, non-critical feature broken
- LOW: Cosmetic issues, warnings, deprecated usage"""

# Sample error logs to triage
ERROR_LOGS = [
    {
        "name": "Connection Error",
        "log": """Traceback (most recent call last):
  File "app.py", line 42, in process_payment
    result = gateway.charge(amount, card_token)
  File "gateway.py", line 18, in charge
    response = requests.post(url, json=payload, timeout=5)
requests.exceptions.ConnectionError: Max retries exceeded with url: /api/v1/charge""",
    },
    {
        "name": "Memory Error",
        "log": """Traceback (most recent call last):
  File "data_pipeline.py", line 156, in load_dataset
    df = pd.read_csv(filepath)
  File "pandas/io/parsers.py", line 685, in read_csv
    return _read(filepath_or_buffer, kwds)
MemoryError: Unable to allocate 8.00 GiB for an array with shape (1073741824,) and data type float64""",
    },
    {
        "name": "Deprecation Warning",
        "log": """DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a
future version. Use datetime.datetime.now(datetime.UTC) instead.
  timestamp = datetime.datetime.utcnow()""",
    },
]


def triage_error(error_log, name="Unknown"):
    """Send an error log to the LLM for triage."""
    response = get_completion(
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": f"Triage this error:\n\n{error_log}"},
        ],
        temperature=0.0,
    )
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw": response}


def main():
    show_config()
    print("\n🐛 Bug Triager — Lab 1.4")
    print("=" * 60)

    for error in ERROR_LOGS:
        print(f"\n📋 Triaging: {error['name']}")
        print(f"{'─'*40}")
        print(f"Log:\n{error['log'][:200]}...")
        print(f"{'─'*40}")

        result = triage_error(error["log"], error["name"])
        print(f"Triage Result:\n{json.dumps(result, indent=2)}")
        print(f"{'='*60}")


if __name__ == "__main__":
    main()
