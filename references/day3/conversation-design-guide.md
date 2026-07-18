# Conversation Design Guide

A reference for designing and building multi-turn chatbots with LLMs.

---

## The Statefulness Problem

LLM APIs are stateless. Every request is independent. Your application must:

1. Store conversation history (list of message dicts)
2. Send the full history with each request
3. Manage history size to stay within context window limits

```python
# The fundamental chatbot loop
conversation = [SYSTEM_MESSAGE]

while True:
    user_input = input("You: ")
    conversation.append({"role": "user", "content": user_input})

    response = get_completion(conversation)
    print(f"Bot: {response}")

    conversation.append({"role": "assistant", "content": response})
```

---

## Context Window Management

### Strategy 1: Truncation

Drop oldest messages when the conversation exceeds a token limit.

```python
def truncate(conversation, max_tokens=8000):
    system = [conversation[0]]
    recent = conversation[1:]
    while count_tokens(system + recent) > max_tokens and recent:
        recent.pop(0)
    return system + recent
```

**Pros:** Simple, predictable
**Cons:** Loses old context permanently

### Strategy 2: Summarization

Ask the LLM to compress old messages into a summary.

```python
def summarize(conversation, keep_recent=6):
    if len(conversation) <= keep_recent + 1:
        return conversation
    system = conversation[0]
    old = conversation[1:-keep_recent]
    recent = conversation[-keep_recent:]
    summary = get_completion([
        {"role": "system", "content": "Summarize in 2-3 sentences. "
         "Preserve key facts and decisions."},
        {"role": "user", "content": str(old)},
    ], temperature=0.0)
    return [system,
            {"role": "system", "content": f"Earlier: {summary}"},
            *recent]
```

**Pros:** Preserves key information
**Cons:** Extra API call, summary may miss details

### Strategy 3: Sliding Window

Keep only the last N turns.

```python
def sliding_window(conversation, max_turns=10):
    system = [conversation[0]]
    turns = conversation[1:]
    if len(turns) > max_turns * 2:
        turns = turns[-(max_turns * 2):]
    return system + turns
```

**Pros:** Simple, bounded cost
**Cons:** Loses early context (e.g., user's name from turn 1)

---

## Chatbot Design Checklist

Before writing code, define:

- [ ] **Purpose:** What does this chatbot do? (one sentence)
- [ ] **Audience:** Who uses it?
- [ ] **Persona:** What personality and tone?
- [ ] **Scope:** What topics are in/out of scope?
- [ ] **Tone:** Formal, casual, technical, friendly?
- [ ] **Limitations:** What can't it do? What should it refuse?
- [ ] **Fallback:** What happens when it can't answer?

---

## System Message Template

```python
SYSTEM_MESSAGE = """You are [NAME], a [PERSONA] [ROLE].

AUDIENCE: [who uses this]
TONE: [communication style]

CAPABILITIES:
- [what it can do 1]
- [what it can do 2]

LIMITATIONS:
- [what it cannot/should not do]

RULES:
- [behavioral rule 1]
- [behavioral rule 2]

DO NOT:
- [anti-behavior 1]
- [anti-behavior 2]"""
```

---

## Edge Case Handling

| Scenario | Strategy |
|:---------|:---------|
| Off-topic | Redirect politely to scope |
| Ambiguous | Ask clarifying question |
| Frustration | Acknowledge, empathize, then help |
| Empty input | Prompt gently |
| Harmful request | Decline clearly |
| Repeated question | Rephrase answer, add detail |

---

## Token Counting

```python
import tiktoken

def count_tokens(messages, model="gpt-4o"):
    enc = tiktoken.encoding_for_model(model)
    total = 0
    for msg in messages:
        total += len(enc.encode(msg["content"]))
        total += 4  # per-message overhead
    return total
```

---

## Commands Pattern

Add slash commands for user control:

| Command | Action |
|:--------|:-------|
| `/clear` | Reset conversation history |
| `/history` | Show current messages |
| `/summary` | Summarize and compress history |
| `/tokens` | Show token count |
| `/temp 0.3` | Adjust temperature |
| `/persona` | Switch chatbot persona |
