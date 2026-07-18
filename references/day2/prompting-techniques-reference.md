# Prompting Techniques Reference

A cheat sheet for the major prompting techniques covered in Day 2.

---

## Zero-Shot Prompting

Direct instruction with no examples. The model relies on its training.

```python
messages = [
    {"role": "system", "content": "Classify as POSITIVE, NEGATIVE, or NEUTRAL."},
    {"role": "user", "content": "The new feature is great!"},
]
```

**When to use:** Simple, well-defined tasks (classification, summarization, translation)
**When it fails:** Ambiguous tasks, domain-specific labels, unusual formats

---

## Few-Shot Prompting

Provide 2-5 examples to teach the model your pattern.

### Message-Based (recommended)
```python
messages = [
    {"role": "system", "content": "Classify sentiment."},
    {"role": "user", "content": "Best purchase ever!"},
    {"role": "assistant", "content": "POSITIVE"},
    {"role": "user", "content": "Waste of money."},
    {"role": "assistant", "content": "NEGATIVE"},
    {"role": "user", "content": "It's fine."},
    {"role": "assistant", "content": "NEUTRAL"},
    {"role": "user", "content": "Pretty good but expensive."},
]
```

### In-Prompt (compact)
```python
user = """Classify:
"Love it!" → POSITIVE
"Hate it." → NEGATIVE
"It's okay." → NEUTRAL
"Pretty good but expensive." → """
```

### Best Practices
- Use **3-5 examples** (enough to show pattern, not too many tokens)
- **Balance categories** (don't show 4 positive and 1 negative)
- **Include edge cases** (mixed sentiment, sarcasm)
- **Order matters**: most representative examples first and last

---

## Chain-of-Thought (CoT)

Ask the model to show its reasoning before giving the final answer.

### Basic CoT
```python
user = "How many Rs are in 'strawberry'? Think step by step."
```

### Structured CoT
```python
system = """For each question, respond in this format:
ANALYSIS: [step-by-step reasoning]
CONCLUSION: [final answer]
CONFIDENCE: [HIGH/MEDIUM/LOW]"""
```

### Plan-and-Execute CoT
```python
system = """First, outline your plan in numbered steps.
Then execute each step.
Finally, state your conclusion."""
```

**When to use:** Multi-step math, logic problems, code debugging, complex analysis
**When it's overkill:** Simple classification, extraction, translation

### Self-Consistency (advanced)
Run the same CoT prompt N times and take the majority answer:
```python
answers = [get_completion(messages) for _ in range(5)]
final_answer = max(set(answers), key=answers.count)
```

---

## Role Prompting

Assign a persona to shape response style, depth, and focus.

```python
system = "You are a senior Python developer with 15 years of experience specializing in Django, PostgreSQL, and distributed systems."
```

### Effective Roles

| Role | Effect |
|:-----|:-------|
| "Senior security engineer" | Focuses on vulnerabilities, OWASP |
| "Patient tutor for beginners" | Simple language, more examples |
| "Technical writer" | Structured, clear, well-organized |
| "Strict code reviewer" | Catches more issues, less forgiving |
| "DevOps engineer" | Mentions CI/CD, monitoring, infra |

### Role + Constraints
```python
system = """You are a senior code reviewer at a fintech company.
You follow these standards:
- PEP 8 compliance
- Type hints required
- Security-first mindset
- No magic numbers
Respond as a numbered list of findings with severity."""
```

---

## Structured Output

### Prompt-Based
```python
system = """Respond with ONLY valid JSON:
{
    "name": "string",
    "email": "string or null",
    "skills": ["array", "of", "strings"]
}"""
```

### JSON Mode (OpenAI)
```python
response = litellm.completion(
    model="gpt-4o",
    messages=messages,
    response_format={"type": "json_object"},
)
```

### Robust Parsing
```python
def parse_json(text):
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Remove markdown fences
        if text.startswith("```"):
            text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        return json.loads(text)
```

---

## Combining Techniques

The most effective prompts combine multiple techniques:

```python
messages = [
    # ROLE + FORMAT (system)
    {"role": "system", "content":
        "You are a senior Python developer. "
        "Think step by step when analyzing code. "           # CoT
        "Respond as JSON: {issues: [], score: int}."},       # Structured

    # FEW-SHOT EXAMPLES
    {"role": "user", "content": "Review: def add(a,b): return a+b"},
    {"role": "assistant", "content": '{"issues": ["no type hints"], "score": 7}'},

    # ACTUAL REQUEST (zero-shot for the specific input)
    {"role": "user", "content": f"Review:\n```python\n{code}\n```"},
]
```

---

## Decision Guide: Which Technique?

| Situation | Start With | Upgrade To |
|:----------|:-----------|:-----------|
| Standard NLP task | Zero-shot | Few-shot if inconsistent |
| Custom classification | Few-shot | More examples if edge cases fail |
| Math/logic problems | CoT | Self-consistency if unreliable |
| Domain-specific task | Role + few-shot | Add CoT for complex reasoning |
| Production system | Few-shot + structured | JSON mode + validation |
