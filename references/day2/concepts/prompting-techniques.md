# Prompting Techniques

Reference for generative tasks, the anatomy of a prompt, core prompting techniques, and responsible prompting.

---

## Generative Tasks

One general model handles many tasks. The prompt decides which one you get.

| Task | What the model does |
| :--- | :--- |
| **Completion** | Continue or fill in text |
| **Dialogue** | Hold a multi-turn conversation |
| **Summarization** | Condense long text to key points |
| **Code generation** | Write or explain code |
| **Labeling** | Classify or extract structured fields |

## Anatomy of a Prompt

A good prompt has four parts:

- **System message:** the role, rules, and tone, persistent across the chat.
- **Context:** the data the model needs for this task.
- **Instruction:** the specific request.
- **Output format:** how the response should be shaped.

The system message sets behavior for the whole conversation; the user message carries the request and data for one turn.

```python
messages = [
    {"role": "system", "content": "You are a concise technical writer."},
    {"role": "user", "content": "Explain what a token is in two sentences."},
]
```

Specific instructions are the cheapest way to improve output. State the format, the constraints, and provide the data the model needs.

## Techniques

### Zero-Shot

Give the task with no examples. The model relies on what it already knows. Try zero-shot first: it works well for standard tasks and costs the fewest tokens.

```python
system = "Classify the sentiment as POSITIVE, NEGATIVE, or NEUTRAL."
user = "The update completely broke my workflow."   # Output: NEGATIVE
```

### Few-Shot

Provide 2 to 5 examples to teach the model your pattern and format. Use 3 to 5 examples, cover edge cases, balance the categories, and remember that order matters (strong examples first and last). Few-shot teaches format, style, and edge-case handling.

### Chain-of-Thought

Ask the model to reason step by step before answering. Use it for math, logic, and multi-step problems; skip it for simple classification. The trigger phrase is "think step by step."

### Role Prompting

Assign a persona to shape depth, style, and focus. "You are a senior Python developer who values clean code and type hints" produces a different answer from a generic prompt.

### Structured Output

Ask for a specific format, such as JSON, so your code can parse the result. Structured output turns an LLM into a dependable component inside a larger program.

```python
system = ('Extract the fields and reply with JSON only: '
          '{"name": str, "amount": number, "due_date": str}')
```

## Responsible Prompting

Three failure modes matter most when input comes from untrusted users or fetched content:

- **Prompt injection:** user input carries instructions that override yours.
- **Prompt leaking:** the model reveals your hidden system prompt.
- **Prompt hijacking:** input redirects the model to a different task.

Mitigations layer together; no single fix is complete:

- Keep instructions separate from user-supplied data.
- Treat retrieved and user text as data, never as commands.
- Validate and filter output before acting on it.
- Give tools the least privilege they need.
