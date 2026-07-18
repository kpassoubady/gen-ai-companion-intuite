# The Transformer Architecture: Simplified

A reference for students who want to understand the "engine" behind LLMs.

---

## The Core Idea

Before Transformers (2017), language models processed text **one word at a time** (RNNs, LSTMs). Transformers changed everything by processing **all words simultaneously** using a mechanism called **self-attention**.

---

## How It Works (Simplified)

### Step 1: Tokenization
```
"The cat sat on the mat" → [The, cat, sat, on, the, mat]
                         → [1234, 5678, 9012, 3456, 1234, 7890]
```

### Step 2: Embedding
Each token ID becomes a **vector** (list of numbers) that captures meaning:
```
"cat"  → [0.12, -0.34, 0.56, ...] (768 dimensions in GPT-2)
"dog"  → [0.11, -0.30, 0.52, ...] (nearby in vector space, similar meaning!)
"table"→ [0.89, 0.23, -0.67, ...] (far away, different meaning)
```

### Step 3: Self-Attention
For each word, the model asks: **"Which other words should I pay attention to?"**

```
"The bank was closed because it was a holiday"
                     ↑
         "bank" attends to "closed" and "holiday"
         → concludes: financial institution (not riverbank)
```

### Step 4: Feed-Forward Networks
After attention, each position passes through a neural network to transform the representation.

### Step 5: Repeat
GPT-4 has **120+ Transformer blocks** stacked on top of each other. Each layer refines the understanding.

### Step 6: Predict Next Token
The final layer outputs a **probability distribution** over all possible next tokens:
```
"The cat sat on the" → {mat: 12%, floor: 8%, roof: 5%, couch: 4%, ...}
```
The model samples from this distribution (controlled by temperature).

---

## Key Insight: Attention is O(n²)

Self-attention compares **every token to every other token**. For a sequence of length n:
- Compute: n² attention scores
- This is why context windows have limits
- A 128K token context = 128,000² = 16.4 billion attention computations!

---

## Parameters = Knowledge

| Model | Parameters | Analogy |
|:------|:----------|:--------|
| GPT-2 | 1.5 billion | A well-read college student |
| GPT-3 | 175 billion | An expert in many fields |
| GPT-4 | ~1.8 trillion (estimated) | A team of experts |
| Llama 3.1 | 8B / 70B / 405B | Choose your size |

Parameters are the **weights** (numbers) the model learned during training. More parameters = more patterns learned = better performance (usually).

---

## Pre-training vs Fine-tuning vs Prompting

| Stage | What Happens | Cost | Who Does It |
|:------|:------------|:-----|:------------|
| **Pre-training** | Learn language from the internet | $10M-$100M+ | OpenAI, Google, Meta |
| **Fine-tuning** | Specialize on a specific domain/task | $100-$10K | Companies |
| **RLHF** | Align with human preferences | $1M+ | Model providers |
| **Prompting** | Guide behavior with instructions | $0.001/call | You! (this course) |

> This course focuses on prompting, the most accessible and cost-effective way to get value from LLMs.

---

## Further Reading

- "Attention Is All You Need" (2017): the original Transformer paper
- Jay Alammar's "The Illustrated Transformer": best visual explanation
- Andrej Karpathy's "Let's build GPT": build a tiny Transformer from scratch
