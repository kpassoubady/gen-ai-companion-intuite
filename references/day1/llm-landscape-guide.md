# LLM Landscape Guide

A reference for choosing the right model for the job.

---

## Model Comparison Table (Updated 2025)

| Model | Provider | Context | Strengths | Pricing (per 1M tokens) |
|:------|:---------|:--------|:----------|:-----------------------|
| **GPT-4o** | OpenAI | 128K | Best all-rounder, strong reasoning | $2.50 in / $10 out |
| **GPT-4o-mini** | OpenAI | 128K | Fast, cheap, good for simple tasks | $0.15 in / $0.60 out |
| **Claude 3.5 Sonnet** | Anthropic | 200K | Best for long documents, coding | $3.00 in / $15 out |
| **Claude 3.5 Haiku** | Anthropic | 200K | Fast, cheap Anthropic option | $0.25 in / $1.25 out |
| **Gemini 2.5 Pro** | Google | 1M | Largest context window | $1.25 in / $10 out |
| **Gemini 2.0 Flash** | Google | 1M | Free tier available, fast | $0.10 in / $0.40 out |
| **Llama 3.1 70B** | Meta (open) | 128K | Self-hosted, no data leaves | Free (compute cost) |
| **Mistral Large** | Mistral (open) | 128K | Strong European option | $2.00 in / $6.00 out |
| **Phi-3 Medium** | Microsoft (open) | 128K | Small but capable, edge deployment | Free (compute cost) |

> Prices change frequently. Check provider pricing pages for current rates.

---

## Decision Matrix

### By Use Case

| Use Case | Recommended Model | Why |
|:---------|:-----------------|:----|
| Quick prototyping | GPT-4o-mini / Gemini Flash | Cheap, fast iteration |
| Production chatbot | GPT-4o / Claude Sonnet | Reliable, well-rounded |
| Code generation | Claude Sonnet / GPT-4o | Top coding benchmarks |
| Document analysis (long) | Gemini 2.5 Pro | 1M token context |
| Summarization | Any capable model | All do well here |
| Classification | GPT-4o-mini / Gemini Flash | Simple task, save money |
| Creative writing | Claude Sonnet / GPT-4o | Best prose quality |
| Data extraction (JSON) | GPT-4o-mini with JSON mode | Structured output support |
| Privacy-sensitive | Llama 3.1 / Mistral (self-hosted) | Data stays on-premise |
| Multilingual | GPT-4o / Gemini Pro | Best language coverage |

### By Constraint

| Constraint | Approach |
|:-----------|:---------|
| Budget < $10/month | Gemini Flash (free tier) or GPT-4o-mini |
| Must be self-hosted | Llama 3.1, Mistral, Phi-3 |
| Must handle 500+ page docs | Gemini 2.5 Pro (1M context) |
| Need fastest response | GPT-4o-mini, Gemini Flash |
| Regulatory (EU data residency) | Mistral (EU-based) or self-hosted |

---

## Open Source vs Closed Source

### Closed Source (API-only)

* **Pros:** Highest quality, no infrastructure to manage, always up-to-date
* **Cons:** Data leaves your control, ongoing costs, vendor lock-in

### Open Source / Open Weight

* **Pros:** Full control, data stays local, one-time compute cost, customizable
* **Cons:** Need GPU infrastructure, lower quality for same size, you manage updates

### Hybrid Approach (Recommended for Production)
1. Use **closed-source API** for development and prototyping
2. Evaluate **open-source alternatives** before production
3. Use **open-source for sensitive data**, closed for general tasks
4. Implement **model fallback**: if primary is down, route to backup

---

## Benchmarks to Watch

| Benchmark | Tests | Leaders (2025) |
|:----------|:------|:---------------|
| **MMLU** | General knowledge across 57 subjects | GPT-4o, Claude Sonnet |
| **HumanEval** | Code generation (Python) | Claude Sonnet, GPT-4o |
| **MATH** | Mathematical reasoning | GPT-4o, Gemini Pro |
| **MT-Bench** | Multi-turn conversation quality | Claude Sonnet, GPT-4o |
| **GPQA** | Graduate-level science questions | GPT-4o, Claude Sonnet |

> **Caution:** Benchmarks don't always reflect real-world performance. Always test with YOUR specific use case.

---

## Key Terminology

| Term | Meaning |
|:-----|:--------|
| **Parameters** | Number of trainable weights (e.g., 70B = 70 billion) |
| **Context window** | Max input+output tokens per request |
| **TPM** | Tokens per minute (rate limit) |
| **RPM** | Requests per minute (rate limit) |
| **Temperature** | Controls randomness (0 = deterministic) |
| **Top-p** | Alternative to temperature, nucleus sampling |
| **Fine-tuning** | Further training on domain-specific data |
| **RLHF** | Human feedback training for alignment |
| **Quantization** | Compressing model weights to use less memory (e.g., 4-bit) |
