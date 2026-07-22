# Sampling and Decoding

Reference for how a model turns next-token probabilities into text: greedy decoding, temperature, top-k, top-p (nucleus), and beam search. Covers both local `generate()` and API parameters.

---

## From Probabilities to Text

At each step a language model produces a probability distribution over the whole vocabulary. Decoding is the rule that picks the next token from that distribution. The same model can sound repetitive or creative depending on the decoding settings.

- **Greedy:** always take the single most likely token. Deterministic and safe, but can be repetitive.
- **Sampling:** draw a token at random according to the probabilities, optionally reshaped by the knobs below.

## Temperature

Temperature rescales the distribution before sampling. Lower temperature sharpens it toward the top tokens; higher temperature flattens it so lower-probability tokens get a chance.

| Value | Behavior | Use case |
| :--- | :--- | :--- |
| 0.0 | Effectively greedy, always the top token | Code, JSON, classification |
| 0.2 | Consistent with minor variation | Data extraction, technical writing |
| 0.7 | Balanced (default) | General chat, Q&A |
| 1.0 | Creative, more variation | Brainstorming, creative writing |
| 1.2+ | Highly random | Experimental only |

## Top-k

Top-k keeps only the `k` highest-probability tokens and samples from those, discarding the long tail. Small `k` stays close to the most likely tokens; large `k` allows more variety.

## Top-p (Nucleus)

Top-p keeps the smallest set of tokens whose cumulative probability reaches `p`, then samples from that nucleus. Unlike top-k, the size of the set adapts to how confident the model is.

```
Tokens sorted by probability: Paris(45%) Lyon(15%) Marseille(12%) Nice(8%) ...
top_p=0.60 -> keep {Paris, Lyon}                    (60%)
top_p=0.90 -> keep {Paris, Lyon, Marseille, Nice}   (80%)
```

Change either temperature or top_p, not both at once, so the effect stays easy to reason about.

## Beam Search

Beam search keeps the `b` most likely partial sequences (beams) at each step and expands all of them, then returns the highest-scoring complete sequence. It favors high-probability, fluent output and is common for translation and summarization. It is slower and can be repetitive, and it is less suited to open-ended creative text.

## Local generate() vs API

For local models with `transformers`, decoding is controlled through `generate()`.

```python
outputs = model.generate(
    **inputs,
    max_new_tokens=40,
    do_sample=True,      # False for greedy or beam search
    temperature=0.8,
    top_k=50,
    top_p=0.95,
    num_beams=1,         # > 1 enables beam search
)
```

For hosted APIs through `shared/llm_client.py`, you typically control `temperature` and `top_p` only.

```python
from shared import get_completion

response = get_completion(messages, temperature=0.2, top_p=1.0)
```

## Task to Parameters

| Task | temperature | top_p | Notes |
| :--- | :--- | :--- | :--- |
| Code generation | 0.0 | 1.0 | Deterministic, greedy |
| JSON extraction | 0.0 | 1.0 | Deterministic |
| Classification | 0.0 | 1.0 | One-word answers |
| Summarization | 0.3 | 1.0 | Slight variation, faithful |
| General chat | 0.7 | 1.0 | Balanced |
| Creative writing | 0.9 | 0.95 | More variety |
| Brainstorming | 1.0 | 0.9 | Wide range of ideas |
| Translation | 0.0 | 1.0 | Often beam search, num_beams 4 |
