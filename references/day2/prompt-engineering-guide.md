# Prompt Engineering Guide

A reference for writing effective prompts that produce reliable, high-quality output.

---

## The 4 Building Blocks

Every effective prompt contains some or all of these components:

| Block | Purpose | Example |
|:------|:--------|:--------|
| **Instruction** | What to do | "Summarize the following article in 3 bullet points" |
| **Context** | Background info | "You are a senior Python developer at a fintech company" |
| **Input Data** | What to process | The document, code, or text to analyze |
| **Output Format** | How to respond | "Respond as JSON with fields: summary, score, tags" |

---

## Prompt Quality Checklist

Before sending a prompt, check:

- [ ] **Clear instruction:** starts with a verb, one task per prompt
- [ ] **Specific scope:** narrowed to exactly what you need
- [ ] **Relevant context:** audience, domain, constraints
- [ ] **Explicit format:** JSON, table, bullets, code block
- [ ] **Length constraint:** word/sentence/paragraph limit
- [ ] **Delimiters:** input data clearly separated from instructions
- [ ] **Temperature:** appropriate for the task (0.0 for code, 0.7 for chat)

---

## Anti-Patterns to Avoid

### 1. Vague Instructions
```
❌ "Help me with this code"
✅ "Review this Python function for bugs and suggest fixes"
```

### 2. Leading Questions
```
❌ "Don't you think React is the best framework?"
✅ "Compare React, Vue, and Angular for a large enterprise app"
```

### 3. Conflicting Constraints
```
❌ "Be brief but very detailed"
✅ "Provide a 2-sentence summary, then a detailed breakdown"
```

### 4. No Output Specification
```
❌ "Analyze this data"
✅ "Analyze this data and return JSON: {trend, key_metric, recommendation}"
```

---

## System Message vs User Message

| Content | Put In | Why |
|:--------|:-------|:----|
| Role / persona | **System** | Persists across turns |
| Output format | **System** | Consistent formatting |
| Constraints / rules | **System** | Always applied |
| The actual task | **User** | Changes each request |
| Input data | **User** | Different every time |

### System Message Template

```python
system = """You are a [ROLE] at [CONTEXT].

STYLE: [direct/friendly/formal]
FORMAT: [JSON/table/bullets/markdown]

CONSTRAINTS:
- [Rule 1]
- [Rule 2]

DO NOT:
- [Anti-behavior 1]
- [Anti-behavior 2]"""
```

---

## Using Delimiters

Delimiters clearly separate instructions from input data:

```python
user = f"""
### INSTRUCTIONS
Summarize the key findings from the document below.

### DOCUMENT
---
{document_text}
---

### OUTPUT FORMAT
3 bullet points, one sentence each.
"""
```

Common delimiters: `---`, `"""`, `###`, `===`, `<section>`, `[SECTION]`

---

## The Prompt Iteration Loop

1. **Write:** draft with all 4 building blocks
2. **Test:** run against 5-10 diverse inputs
3. **Analyze:** read every output, note failures
4. **Refine:** fix the specific failure mode
5. **Repeat:** test again, fix next failure

Plan for 3-5 iterations minimum. A prompt is never done on the first try.

---

## Goal-First Prompting

Work backwards from the desired output:

1. Write the **exact expected output** first
2. Define what **format** it should be in
3. Identify what **context** the model needs
4. Write the **instruction** that produces it

```python
# Step 1: Expected output
# {"category": "billing", "priority": "high", "requires_human": true}

# Step 2-4: Work backwards to the prompt
system = """Classify support tickets.
Category: billing, technical, account, feature_request, other.
Priority: high, medium, low.
Set requires_human: true if human intervention is needed.
Respond with ONLY valid JSON."""
```

---

## Quick Reference: Prompt Starters

| Task | Good Opening |
|:-----|:-------------|
| Summarize | "Summarize the following in X bullet points..." |
| Classify | "Classify the following as exactly one of: A, B, C..." |
| Extract | "Extract the following fields from the text as JSON..." |
| Review | "Review the following code for bugs, security issues, and..." |
| Generate | "Write a Python function that..." |
| Compare | "Compare X and Y for use case Z. Consider..." |
| Explain | "Explain X to a [audience]. Include..." |
| Refactor | "Refactor the following code. Maintain the same behavior..." |
