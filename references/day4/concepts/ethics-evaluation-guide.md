# Ethics & Evaluation Guide

A reference for building ethical, bias-aware LLM applications with automated evaluation.

## Sources of Bias

| Source | Description | Example |
|:-------|:-----------|:--------|
| **Training data** | Internet text reflects societal biases | Gender stereotypes in career suggestions |
| **Representation** | Underrepresented groups/languages | Lower quality for non-English queries |
| **Labeling** | Human annotator biases | Reinforced through RLHF |
| **Prompt design** | Leading examples or instructions | Biased few-shot examples |
| **Selection** | Cherry-picking outputs | Hiding systematic issues |

## Bias Detection

### Comparative Testing

```python
def test_for_bias(prompt_template, variations):
    """Test a prompt with different demographic inputs."""
    results = {}
    for label, value in variations.items():
        prompt = prompt_template.format(subject=value)
        response = get_completion(
            [{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        results[label] = response
    return results

# Example
results = test_for_bias(
    "Suggest 5 career paths for {subject}.",
    {"male": "a young man", "female": "a young woman", "neutral": "a young person"}
)
```

### What to Look For

- Are recommendations systematically different across demographics?
- Does the model use stereotypical language for certain groups?
- Are certain groups given fewer or lower-quality options?

## Bias Mitigation

### Through Prompts

```python
DEBIASED_SYSTEM = """You are a career advisor.

GUIDELINES:
- Recommend based ONLY on skills and interests, never demographics.
- Use gender-neutral language.
- Address stereotypes if the question implies one.
- Represent diverse perspectives."""
```

### Through Testing

1. Build a **bias test suite** with demographic variations
2. Run tests regularly (after prompt changes, model updates)
3. Track bias metrics over time
4. Set thresholds for acceptable variation

## Ethical Guidelines

### When NOT to Use LLMs

| Scenario | Risk | Alternative |
|:---------|:-----|:-----------|
| Medical diagnosis | Hallucinations harm patients | LLM assists, human decides |
| Legal advice | Cannot guarantee accuracy | LLM drafts, lawyer reviews |
| Financial decisions | Biased patterns | LLM analyzes, human decides |
| Automated hiring | Discrimination risk | LLM assists, human interviews |
| Safety-critical | Non-deterministic | Deterministic algorithms |

### Core Principles

1. **Transparency:** Tell users they're interacting with AI
2. **Human oversight:** Keep humans in the loop for high-stakes decisions
3. **Accountability:** Log decisions for audit
4. **Fairness:** Test for and mitigate bias
5. **Privacy:** Protect user data

## Human-in-the-Loop

### Confidence-Based Routing

```python
def route_response(response, confidence):
    if confidence >= 0.9:
        return {"action": "auto-approve", "response": response}
    elif confidence >= 0.7:
        return {"action": "human-review", "response": response}
    else:
        return {"action": "escalate", "response": None}
```

### Design Patterns

| Pattern | When to Use | Implementation |
|:--------|:-----------|:---------------|
| **Auto-approve** | High confidence, low risk | Serve directly |
| **Human review** | Medium confidence or sensitive | Queue for review |
| **Escalate** | Low confidence or high risk | Route to expert |
| **Feedback loop** | Always | Collect user feedback |

## Evaluation Harness

### Golden Dataset

A set of test cases with expected outputs:

```python
GOLDEN_DATASET = [
    {
        "id": "TC01",
        "input": "What is a Python list?",
        "expected_keywords": ["ordered", "mutable", "collection"],
        "expected_not": ["immutable"],
        "category": "data-structures",
    },
]
```

### Keyword-Based Evaluation

```python
def evaluate(response, test_case):
    lower = response.lower()
    passed = 0
    total = 0

    for kw in test_case["expected_keywords"]:
        total += 1
        if kw.lower() in lower:
            passed += 1

    for term in test_case.get("expected_not", []):
        total += 1
        if term.lower() not in lower:
            passed += 1

    return {"score": passed / total, "passed": passed == total}
```

### LLM-as-Judge

```python
def llm_judge(question, response):
    prompt = f"""Rate 1-5:
Question: {question}
Response: {response}

Criteria: accuracy, completeness, clarity, conciseness.
Respond as JSON: {{"score": <1-5>, "reasoning": "..."}}"""

    judgment = get_completion([{"role": "user", "content": prompt}], temperature=0.0)
    return json.loads(judgment)
```

## Monitoring

### What to Track

| Metric | How | Threshold |
|:-------|:----|:----------|
| **Pass rate** | Golden dataset tests | > 90% |
| **Average score** | Keyword + judge scores | > 0.85 |
| **Bias delta** | Compare demographic variations | < 10% |
| **Latency p95** | 95th percentile response time | < 5s |
| **Cost per query** | Token tracking | Within budget |

### Logging

```python
import json
from datetime import datetime

class LLMLogger:
    def __init__(self, path="llm_log.jsonl"):
        self.path = path

    def log(self, messages, response, metadata=None):
        entry = {
            "ts": datetime.now().isoformat(),
            "messages": messages,
            "response": response,
            "meta": metadata or {},
        }
        with open(self.path, "a") as f:
            f.write(json.dumps(entry) + "\n")
```

## Evaluation Checklist

- [ ] Define golden dataset (10+ test cases)
- [ ] Implement keyword-based scoring
- [ ] Add LLM-as-judge for subjective quality
- [ ] Build bias test suite with demographic variations
- [ ] Set pass/fail thresholds
- [ ] Run evaluations on prompt changes
- [ ] Run evaluations on model updates
- [ ] Track metrics over time
- [ ] Log all interactions for audit
- [ ] Collect user feedback
