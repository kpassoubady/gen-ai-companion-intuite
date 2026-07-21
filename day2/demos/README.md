# Day 2 Demos

Instructor demo scripts for Day 2. Every demo runs without an API key. They use
either small Hugging Face models that download once and cache locally, or pure
Python with no downloads at all.

## Setup

The demos run on local models, so no `.env` or provider key is required. Install
the demo dependencies once:

```bash
pip install tiktoken transformers torch scikit-learn sentence-transformers numpy
```

First run of a model-backed demo downloads the model from Hugging Face and
caches it under `~/.cache/huggingface`. After that, the demo runs offline. Run
each model-backed demo once before class on the machine you will present from so
the download happens ahead of time.

Approximate first-run download sizes:

| Model | Used by | Size |
| :--- | :--- | :--- |
| `bert-base-uncased` | tokenization, contextual embeddings | ~420 MB |
| `all-MiniLM-L6-v2` | bow vs embeddings | ~80 MB |
| `gpt2` | autoregressive, hugging face tour | ~500 MB |
| `distilbert-base-uncased` | hugging face tour | ~270 MB |
| `google/flan-t5-base` | prompting techniques | ~1 GB |

To shrink the prompting download, set `MODEL_NAME = "google/flan-t5-small"` in
`demo-prompting-techniques.py`.

## Demos by session

### Session 1: NLP - Understanding Language as Data

| Demo | Shows | Needs download |
| :--- | :--- | :--- |
| `demo-tokenization.py` | BPE vs WordPiece, token IDs, token counts | yes (bert) |
| `demo-bow-vs-embeddings.py` | bag-of-words limits vs embedding similarity | yes (minilm) |

### Session 2: Large Language Models

| Demo | Shows | Needs download |
| :--- | :--- | :--- |
| `demo-autoregressive.py` | generation as next-token prediction | yes (gpt2) |
| `demo-huggingface-tour.py` | one pipeline API across three tasks | yes (gpt2, distilbert) |
| `demo-contextual-embeddings.py` | BERT gives context-dependent vectors | yes (bert) |

### Session 3: Language Generation Tasks & Prompting

| Demo | Shows | Needs download |
| :--- | :--- | :--- |
| `demo-prompting-techniques.py` | zero-shot, few-shot, chain-of-thought | yes (flan-t5) |
| `demo-prompt-injection.py` | injection, leaking, hijacking, mitigations | no |

### Session 4: Agentic AI

| Demo | Shows | Needs download |
| :--- | :--- | :--- |
| `demo-function-calling.py` | the function-calling loop | no |
| `demo-react-agent.py` | ReAct thought, action, observation loop | no |

## Running a demo

From the repository root:

```bash
python3 day2/demos/demo-tokenization.py
```

## Notes 

- The pure-Python demos (`demo-prompt-injection.py`, `demo-function-calling.py`,
  `demo-react-agent.py`) use a small scripted stand-in for the model so the
  mechanism is visible and the output is deterministic. In production the LLM
  performs the "decide" step; the surrounding loop is identical.
- `demo-prompting-techniques.py` uses `google/flan-t5-base`, a small
  instruction-tuned model. It handles classification well and shows chain-of-
  thought flipping a wrong direct answer into a correct one. A small model is
  weaker at reasoning than a hosted API model, which reinforces that model
  choice matters. The prompting techniques themselves transfer unchanged to any
  provider.
