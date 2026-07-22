# RAG Evaluation

Reference for measuring RAG quality: LLM-as-a-judge, retrieval recall@k, answer faithfulness, and context relevance, with a small golden-set approach.

---

## Why Evaluate

A RAG system can fail at retrieval (wrong chunks) or at generation (wrong answer from right chunks). Evaluation separates these so you know what to fix. Track a small set of metrics over a fixed test set as you change chunking, embeddings, or prompts.

## Golden Set

A golden set is a small collection of questions with reference answers and, where possible, the source chunks that should be retrieved. Even ten to twenty examples give a useful signal. Run the RAG system over the set, score each answer, and watch the scores move as you tune the system.

## Retrieval Metrics

**Recall@k** measures whether the correct source chunk appears in the top-k retrieved chunks. If you labeled the expected source for each question, recall@k is the fraction of questions whose expected chunk was retrieved within the top k.

- Low recall@k means the retriever is missing relevant chunks. Fix chunking or the embedding model, or raise k.
- High recall@k with bad answers points at the generation step, not retrieval.

## Answer Metrics

- **Faithfulness (groundedness):** does the answer only make claims supported by the retrieved context? Unsupported claims are hallucinations.
- **Context relevance:** are the retrieved chunks actually about the question, or is the context noisy?
- **Answer quality:** does the answer address the question clearly and completely?

## LLM-as-a-Judge

An LLM-as-a-judge scores answers automatically by prompting a capable model with the question, the context, and the answer, and asking for a score on each dimension. This scales better than manual review and correlates reasonably well with human ratings for coarse scoring.

```python
JUDGE = """You are grading a RAG answer. Given the question, the retrieved
context, and the answer, score each item from 1 to 5 and return JSON:
{"faithfulness": n, "context_relevance": n, "answer_quality": n}

Faithfulness: are all claims supported by the context?
Context relevance: is the context about the question?
Answer quality: is the answer clear and complete?"""

def judge(question, context, answer):
    messages = [
        {"role": "system", "content": JUDGE},
        {"role": "user", "content":
         f"Question: {question}\nContext: {context}\nAnswer: {answer}"},
    ]
    return get_completion(messages, tier="mini", temperature=0.0)
```

Keep the judge at temperature 0.0 for stable scores, and use a separate model or prompt from the one that generated the answer where you can.

## Metrics Summary

| Metric | What it measures | Low score means |
| :--- | :--- | :--- |
| **Recall@k** | Correct chunk in top-k | Retriever misses relevant text |
| **Faithfulness** | Claims supported by context | Model is hallucinating |
| **Context relevance** | Retrieved context on-topic | Noisy or wrong retrieval |
| **Answer quality** | Clear, complete answer | Generation or prompt needs work |

## Observability

Log the query, the retrieved chunk ids and scores, the final prompt, and the answer for each request. When an answer is wrong, these logs show whether retrieval or generation failed, which is faster than guessing. Aggregate judge scores over time to catch regressions after a change.
