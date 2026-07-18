"""
Lab: Bug Triager
Goal: Build a tool that classifies error logs by severity and outputs strict JSON.

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

ERROR_LOG = """Traceback (most recent call last):
  File "app.py", line 42, in process_payment
    result = gateway.charge(amount, card_token)
  File "gateway.py", line 18, in charge
    response = requests.post(url, json=payload, timeout=5)
requests.exceptions.ConnectionError: Max retries exceeded with url: /api/v1/charge"""

def triage_error(error_log):
    """Send an error log to the LLM and return parsed JSON."""
    # TODO: Implement this function
    # 1. Create messages array
    # 2. Call get_completion (Hint: temperature=0.0 since we want strict JSON format)
    # 3. Parse the JSON response into a Python dictionary using json.loads()
    # 4. Return the dictionary

    return {"error": "TODO: Implement the triage_error function!"}

def main():
    show_config()
    print("\n🐛 Bug Triager")
    print("=" * 60)

    print(f"\n📋 Triaging Connection Error...")
    print(f"Log:\n{ERROR_LOG}")
    print(f"{'─'*40}")

    result = triage_error(ERROR_LOG)
    print(f"Triage Result:\n{json.dumps(result, indent=2)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
