# LLM API Quick Reference

Cheat sheet for the LLM API patterns used in this course.

---

## Basic Call

```python
from shared import get_completion

response = get_completion(
    messages=[{"role": "user", "content": "Hello!"}],
    tier="mini",       # "mini" = fast/cheap, "default" = capable
    temperature=0.7,   # 0.0 = deterministic, 1.0+ = creative
    max_tokens=1024,   # max response length
)
print(response)  # string
```

---

## Full Response (with metadata)

```python
from shared import get_completion_full

response = get_completion_full(
    messages=[{"role": "user", "content": "Hello!"}],
)

# Response content
print(response.choices[0].message.content)

# Token usage
print(response.usage.prompt_tokens)
print(response.usage.completion_tokens)
print(response.usage.total_tokens)

# Stop reason
print(response.choices[0].finish_reason)  # "stop" | "length" | "content_filter"
```

---

## Message Roles

| Role | Purpose | Example |
|:-----|:--------|:--------|
| `system` | Set behavior/persona | "You are a Python expert." |
| `user` | Human input | "Explain decorators." |
| `assistant` | Previous AI response | Used for multi-turn conversations |

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language..."},
    {"role": "user", "content": "How do I install it?"},
]
```

---

## Temperature Guide

| Value | Behavior | Use Case |
|:------|:---------|:---------|
| 0.0 | Always same output | Code, JSON, classification |
| 0.3 | Mostly consistent | Technical writing, summaries |
| 0.7 | Balanced (default) | General Q&A, explanations |
| 1.0 | Creative | Brainstorming, creative writing |
| 1.5+ | Very random | Experimental only |

---

## Common Patterns

### Structured JSON Output
```python
system = "Respond with ONLY valid JSON. No other text."
```

### Classification
```python
system = "Classify as exactly one of: BUG, FEATURE, QUESTION. Respond with only the label."
```

### Step-by-Step Reasoning
```python
user = "Think step by step, then provide your final answer."
```

### Few-Shot (examples in prompt)
```python
user = """Classify the sentiment:
"I love this!" → POSITIVE
"This is terrible" → NEGATIVE
"It's okay I guess" → NEUTRAL
"The sunset was breathtaking" → """
```

---

## Provider Configuration

```bash
# .env file
LLM_PROVIDER=openai          # openai | gemini | claude
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=...
ANTHROPIC_API_KEY=sk-ant-...
```

```python
from shared import show_config
show_config()  # verify setup
```

---

## Token Counting

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
tokens = enc.encode("Hello, world!")
print(f"Token count: {len(tokens)}")
print(f"Token IDs: {tokens}")
print(f"Decoded: {[enc.decode([t]) for t in tokens]}")
```

---

## Error Handling

```python
from shared import get_completion
import litellm

try:
    response = get_completion(messages=[...])
except litellm.exceptions.RateLimitError:
    print("Rate limited. Wait and retry")
except litellm.exceptions.AuthenticationError:
    print("Bad API key. Check .env")
except litellm.exceptions.APIConnectionError:
    print("Network error. Check internet")
except Exception as e:
    print(f"Unexpected error: {e}")
```
