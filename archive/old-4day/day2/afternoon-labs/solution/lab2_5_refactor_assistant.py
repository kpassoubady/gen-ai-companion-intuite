"""
Lab 2.5 — Refactor Assistant (Prompt Iteration)
Day 2 — Session 4

Goal: Build a tool that refactors messy Python code. Iterate the prompt 3 times
      based on observed failures.

Instructions:
1. Start with v1 of the prompt. Run it against the 3 samples. Note failures.
2. Improve to v2: fix the most common failure. Test again.
3. Improve to v3: fix the next failure. Test again.
4. Document what changed at each iteration and why.

Run: python3 day2/labs/lab2_5_refactor_assistant.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from shared import get_completion, show_config


# --- Prompt Versions ---
# Iterate on these! Start with v1, observe failures, improve.

PROMPT_V1 = """Refactor the following Python code to be cleaner."""

PROMPT_V2 = """You are a senior Python developer. Refactor the following code.

Requirements:
- Improve variable names to be descriptive
- Add type hints to function signatures
- Add a docstring explaining the function
- Follow PEP 8 style
- Do NOT change the function's behavior

Respond with:
1. The refactored code in a Python code block
2. A brief list of changes you made"""

PROMPT_V3 = """You are a senior Python developer performing a code review and refactor.

Refactor the following code following these strict rules:
- Rename variables and function to be descriptive (e.g., 'd' → 'users', 'r' → 'results')
- Add type hints to all function parameters and return type
- Add a clear docstring (Google style) explaining purpose, args, and returns
- Follow PEP 8: line length ≤ 88 chars, proper spacing
- Use list comprehension where it improves readability
- Do NOT change the function's external behavior or return type
- Do NOT add error handling unless the original has it

Respond in this exact format:

### Refactored Code
```python
<your refactored code here>
```

### Changes Made
1. <change 1>
2. <change 2>
...

### Why Each Change Improves the Code
1. <explanation 1>
2. <explanation 2>
..."""


# Messy code samples to refactor
SAMPLES = [
    {
        "name": "Filter Active Users",
        "code": '''
def proc(d):
    r = []
    for i in d:
        if i['status'] == 'active' and i['age'] > 18:
            n = i['first'] + ' ' + i['last']
            r.append({'name': n, 'email': i['email']})
    return r
''',
    },
    {
        "name": "Calculate Statistics",
        "code": '''
def calc(l):
    s = 0
    for x in l:
        s = s + x
    a = s / len(l)
    l2 = sorted(l)
    if len(l2) % 2 == 0:
        m = (l2[len(l2)//2-1] + l2[len(l2)//2]) / 2
    else:
        m = l2[len(l2)//2]
    mx = l2[-1]
    mn = l2[0]
    return {'avg': a, 'median': m, 'max': mx, 'min': mn}
''',
    },
    {
        "name": "Flatten Nested Config",
        "code": '''
def f(d, p=''):
    o = {}
    for k, v in d.items():
        nk = p + '.' + k if p else k
        if type(v) == dict:
            o.update(f(v, nk))
        elif type(v) == list:
            for i, item in enumerate(v):
                if type(item) == dict:
                    o.update(f(item, nk + '.' + str(i)))
                else:
                    o[nk + '.' + str(i)] = item
        else:
            o[nk] = v
    return o
''',
    },
]


def refactor_code(code, prompt_version, version_label):
    """Send code to the LLM for refactoring using the specified prompt version."""

    response = get_completion(
        messages=[
            {"role": "system", "content": prompt_version},
            {"role": "user", "content": f"Refactor this code:\n\n```python\n{code}\n```"},
        ],
        temperature=0.0,
    )
    return response



def run_iteration(prompt_version, version_label):
    """Run a prompt version against all samples."""
    print(f"\n{'='*70}")
    print(f"🔄 Prompt Version: {version_label}")
    print(f"{'='*70}")

    for sample in SAMPLES:
        print(f"\n📝 Refactoring: {sample['name']}")
        print(f"{'─'*50}")
        print(f"Original:\n{sample['code']}")
        print(f"{'─'*50}")

        result = refactor_code(sample["code"], prompt_version, version_label)
        print(f"Result:\n{result}")
        print(f"{'='*70}")


def main():
    show_config()
    print("\n🔧 Refactor Assistant — Lab 2.5")
    print("Running 3 iterations of prompt improvement\n")

    # Iteration 1: Basic prompt
    print(">>> ITERATION 1: Basic prompt (observe what fails)")
    run_iteration(PROMPT_V1, "v1 - Basic")

    # Iteration 2: Improved prompt
    print("\n>>> ITERATION 2: Added structure and rules")
    run_iteration(PROMPT_V2, "v2 - Structured")

    # Iteration 3: Refined prompt
    print("\n>>> ITERATION 3: Strict format and detailed rules")
    run_iteration(PROMPT_V3, "v3 - Detailed")

    # Analysis prompt
    print(f"\n{'='*70}")
    print("📊 Your Analysis:")
    print("   Compare the 3 iterations:")
    print("   - v1: What was missing? What failed?")
    print("   - v2: What improved? What still failed?")
    print("   - v3: What improved? Is it good enough to ship?")
    print("   - What would v4 look like?")
    print(f"{'='*70}")

    print("\n✅ Lab 2.5 complete!")


if __name__ == "__main__":
    main()
