# API Parameters Reference

A cheat sheet for all LLM API parameters covered in Day 2.

---

## temperature (0.0 - 2.0)

Controls randomness in token selection. Lower = more deterministic.

| Value | Behavior | Use Case |
|:------|:---------|:---------|
| 0.0 | Always picks the most likely token | Code, JSON, classification |
| 0.2 | Very consistent with minor variation | Technical writing, data extraction |
| 0.3 | Mostly consistent | Summaries, reviews |
| 0.7 | Balanced (default) | General chat, Q&A |
| 1.0 | Creative, more variation | Brainstorming, creative writing |
| 1.2+ | Highly random | Experimental only |

```python
response = get_completion(messages, temperature=0.0)  # deterministic
response = get_completion(messages, temperature=0.7)  # balanced
response = get_completion(messages, temperature=1.0)  # creative
```

---

## top_p (0.0 - 1.0): Nucleus Sampling

Limits the model to tokens whose cumulative probability reaches p.

```
Tokens sorted by probability: Paris(45%) Lyon(15%) Marseille(12%) Nice(8%) ...

top_p=0.6 → considers {Paris, Lyon}             (60%)
top_p=0.9 → considers {Paris, Lyon, Marseille, Nice} (80%)
top_p=1.0 → considers all tokens (default)
```

**Rule:** Change **either** temperature or top_p, not both.

```python
# Creative but within reason
response = get_completion(messages, temperature=1.0, top_p=0.9)
```

---

## frequency_penalty (-2.0 to 2.0)

Penalizes tokens proportional to how often they've appeared.

| Value | Effect |
|:------|:-------|
| 0.0 | No penalty (default) |
| 0.3 | Slight reduction in word repetition |
| 0.5 | Noticeable reduction |
| 1.0+ | Strong avoidance of repeated words |
| Negative | Encourages repetition |

**Best for:** Long-form text, blog posts, creative writing

---

## presence_penalty (-2.0 to 2.0)

Penalizes tokens that have appeared at all (binary, not proportional).

| Value | Effect |
|:------|:-------|
| 0.0 | No penalty (default) |
| 0.3 | Slightly encourages new topics |
| 0.6 | Noticeably encourages topic diversity |
| 1.0+ | Strongly pushes toward new topics |

**Best for:** Brainstorming, avoiding topic loops in conversations

### frequency vs presence

| | frequency_penalty | presence_penalty |
|:--|:-----------------|:-----------------|
| **How** | Proportional to count | Binary (appeared or not) |
| **Effect** | Reduces word repetition | Encourages new topics |
| **For code** | 0.0 | 0.0 |
| **For essays** | 0.3-0.5 | 0.0-0.3 |
| **For brainstorming** | 0.3 | 0.5-0.8 |

---

## max_tokens

Maximum number of tokens the model can generate in its response.

| Scenario | Recommended |
|:---------|:-----------|
| Classification (one word) | 10 |
| Short answer | 100-200 |
| Code snippet | 500-1000 |
| Detailed explanation | 1000-2000 |
| Long-form content | 4096+ |

```python
response = get_completion(messages, max_tokens=200)
```

**Important:** If the model hits this limit, `finish_reason` will be `"length"` instead of `"stop"`. Always check!

---

## stop

List of sequences that cause the model to stop generating.

```python
import litellm
from shared import get_model

response = litellm.completion(
    model=get_model(),
    messages=messages,
    stop=["\ndef ", "\nclass "],  # stop before next function/class
)
```

**Use cases:**
- Generate exactly one function (stop at next `def`)
- Generate one SQL query (stop at `;\n`)
- Generate one paragraph (stop at `\n\n`)

---

## seed

Makes responses more reproducible (not perfectly deterministic).

```python
response = get_completion(messages, temperature=0.7, seed=42)
```

**Use cases:**
- Automated testing: consistent outputs for assertions
- Demos: reproduce the same response
- A/B testing: compare prompt changes with same randomness

**Note:** Even with `seed`, results may vary slightly due to infrastructure changes. Use `seed` + `temperature=0.0` for maximum determinism.

---

## Streaming

Stream tokens as they're generated for real-time display.

```python
import litellm
from shared import get_model

response = litellm.completion(
    model=get_model(),
    messages=messages,
    stream=True,
)

full_text = ""
for chunk in response:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
        full_text += delta
print()
```

**Key differences from non-streaming:**

| Aspect | Non-Streaming | Streaming |
|:-------|:-------------|:----------|
| Return type | Response object | Iterator of chunks |
| Time to first token | Full generation time | ~200ms |
| UX | Blank screen, then full response | Tokens appear in real-time |

---

## Quick Reference: Task → Parameters

| Task | temperature | top_p | freq_penalty | pres_penalty | max_tokens |
|:-----|:-----------|:------|:-------------|:-------------|:-----------|
| Code generation | 0.0 | 1.0 | 0.0 | 0.0 | 1000 |
| JSON extraction | 0.0 | 1.0 | 0.0 | 0.0 | 500 |
| Classification | 0.0 | 1.0 | 0.0 | 0.0 | 10 |
| Technical writing | 0.3 | 1.0 | 0.3 | 0.0 | 2000 |
| Summarization | 0.3 | 1.0 | 0.0 | 0.0 | 500 |
| General chat | 0.7 | 1.0 | 0.0 | 0.0 | 1024 |
| Creative writing | 0.9 | 1.0 | 0.5 | 0.3 | 2000 |
| Brainstorming | 1.0 | 0.9 | 0.3 | 0.6 | 1000 |
