# Cost Optimization Reference

A reference for managing LLM API costs, latency, and error handling in production.

## Token Pricing

### Current Pricing (as of 2025)

| Model | Input (per 1M) | Output (per 1M) | Context Window |
|:------|:---------------|:----------------|:---------------|
| GPT-4o | $2.50 | $10.00 | 128K |
| GPT-4o-mini | $0.15 | $0.60 | 128K |
| Claude 3.5 Sonnet | $3.00 | $15.00 | 200K |
| Gemini 2.5 Pro | $1.25 | $10.00 | 1M |
| Gemini 2.5 Flash | $0.15 | $0.60 | 1M |

**Key insight:** Output tokens cost 3-5x more than input tokens.

### Cost Estimation

```python
import tiktoken

def estimate_cost(messages, response, model="gpt-4o"):
    enc = tiktoken.encoding_for_model(model)
    input_tokens = sum(len(enc.encode(m["content"])) for m in messages)
    output_tokens = len(enc.encode(response))

    PRICING = {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    }

    p = PRICING.get(model, PRICING["gpt-4o-mini"])
    cost = (input_tokens / 1e6) * p["input"] + (output_tokens / 1e6) * p["output"]
    return {"input_tokens": input_tokens, "output_tokens": output_tokens, "cost": cost}
```

## Optimization Strategies

### 1. Model Tiering

Use the cheapest model that meets quality requirements:

```python
def choose_model(task):
    if task in ("greeting", "faq", "simple_classification"):
        return "gpt-4o-mini"
    elif task in ("summarization", "code_explanation"):
        return "gpt-4o-mini"
    else:
        return "gpt-4o"
```

**Rule of thumb:** Start with mini. Upgrade only when quality is insufficient.

### 2. Response Caching

```python
import hashlib
import time

class ResponseCache:
    def __init__(self, ttl=3600):
        self.cache = {}
        self.ttl = ttl

    def get(self, query):
        key = hashlib.md5(query.lower().strip().encode()).hexdigest()
        entry = self.cache.get(key)
        if entry and time.time() - entry["ts"] < self.ttl:
            return entry["response"]
        return None

    def set(self, query, response):
        key = hashlib.md5(query.lower().strip().encode()).hexdigest()
        self.cache[key] = {"response": response, "ts": time.time()}
```

### 3. Prompt Optimization

| Technique | Token Savings | Quality Impact |
|:----------|:-------------|:---------------|
| Remove filler words | 20-40% | None |
| Shorter system prompts | 10-30% | Test carefully |
| Compress RAG context | 20-50% | May lose detail |
| Use `max_tokens` | Variable | May truncate |

### 4. Batch Processing

```python
# Instead of N separate API calls, combine related queries
combined_prompt = "Answer each question below:\n"
for i, q in enumerate(questions):
    combined_prompt += f"\n{i+1}. {q}"
combined_prompt += "\n\nRespond with numbered answers."
```

## Latency Optimization

### Streaming

```python
import litellm

def stream_response(messages):
    response = litellm.completion(
        model="gpt-4o-mini", messages=messages, stream=True
    )
    full = ""
    for chunk in response:
        delta = chunk.choices[0].delta.content or ""
        print(delta, end="", flush=True)
        full += delta
    return full
```

### Parallel Calls

```python
import asyncio
import litellm

async def parallel_queries(queries):
    tasks = [
        litellm.acompletion(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": q}]
        )
        for q in queries
    ]
    return await asyncio.gather(*tasks)
```

## Error Handling

### Common Errors

| Error | Code | Fix |
|:------|:-----|:----|
| Rate limit | 429 | Retry with backoff |
| Server error | 500 | Retry, fallback provider |
| Timeout | 408/504 | Increase timeout |
| Auth error | 401 | Check/rotate API key |
| Context too long | 400 | Truncate input |

### Retry with Exponential Backoff

```python
import time

def retry_with_backoff(func, max_retries=3, base_delay=1.0):
    for attempt in range(max_retries + 1):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries:
                raise
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
```

## Monitoring

### Usage Tracking

```python
class UsageTracker:
    def __init__(self):
        self.calls = []

    def log(self, model, input_tokens, output_tokens, latency_ms):
        self.calls.append({
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "latency_ms": latency_ms,
            "timestamp": time.time(),
        })

    def summary(self):
        total_in = sum(c["input_tokens"] for c in self.calls)
        total_out = sum(c["output_tokens"] for c in self.calls)
        return {
            "calls": len(self.calls),
            "input_tokens": total_in,
            "output_tokens": total_out,
        }
```

### Budget Guards

```python
class BudgetGuard:
    def __init__(self, daily_limit=5.0):
        self.limit = daily_limit
        self.spent = 0.0

    def check(self, est_cost):
        return self.spent + est_cost <= self.limit

    def record(self, cost):
        self.spent += cost
```

## Cost Optimization Checklist

- [ ] Use mini models for simple tasks
- [ ] Cache identical queries
- [ ] Set `max_tokens` to limit output length
- [ ] Remove filler words from prompts
- [ ] Batch related queries when possible
- [ ] Monitor token usage per endpoint
- [ ] Set daily/monthly spending limits
- [ ] Stream responses for better UX
- [ ] Implement retry with exponential backoff
- [ ] Log all API calls with token counts
