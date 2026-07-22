# Day 3 Demos

Instructor demo scripts for Day 3. Every demo runs without an API key. They use
either small Hugging Face models that download once and cache locally, or pure
Python (and PyTorch/NumPy) with no downloads at all.

## Setup

The demos run on local models, so no `.env` or provider key is required. Install
the demo dependencies once:

```bash
pip install torch numpy scikit-learn sentence-transformers transformers
```

First run of a model-backed demo downloads the model from Hugging Face and
caches it under `~/.cache/huggingface`. After that, the demo runs offline. Run
each model-backed demo once before class on the machine you will present from so
the download happens ahead of time.

Approximate first-run download sizes:

| Model | Used by | Size |
| :--- | :--- | :--- |
| `all-MiniLM-L6-v2` | feature extraction | ~80 MB |
| `gpt2` | sampling knobs | ~500 MB |

## Demos by session

### Session 1: Transfer Learning & Fine-Tuning

| Demo | Shows | Needs download |
| :--- | :--- | :--- |
| `demo-feature-extraction.py` ([Colab](notebooks/demo-feature-extraction.ipynb)) | frozen encoder plus a tiny trainable head | yes (minilm) |
| `demo-catastrophic-forgetting.py` ([Colab](notebooks/demo-catastrophic-forgetting.ipynb)) | training on a new task erases an earlier one | no |

### Session 2: PEFT/LoRA & Sampling

| Demo | Shows | Needs download |
| :--- | :--- | :--- |
| `demo-lora-parameters.py` ([Colab](notebooks/demo-lora-parameters.ipynb)) | why LoRA trains so few parameters | no |
| `demo-sampling-knobs.py` ([Colab](notebooks/demo-sampling-knobs.ipynb)) | temperature, top-k, top-p, beam search | yes (gpt2) |

### Session 3: RAG

| Demo | Shows | Needs download |
| :--- | :--- | :--- |
| `demo-chunking.py` ([Colab](notebooks/demo-chunking.ipynb)) | fixed-size vs overlap vs paragraph chunking | no |

### Session 4: Deployment Optimization

| Demo | Shows | Needs download |
| :--- | :--- | :--- |
| `demo-quantization.py` ([Colab](notebooks/demo-quantization.ipynb)) | int8 dynamic quantization shrinks a model | no |
| `demo-pruning.py` ([Colab](notebooks/demo-pruning.ipynb)) | magnitude pruning makes a model sparse | no |

## Running a demo

From the repository root:

```bash
python3 day3/demos/demo-chunking.py
```

## Notes

- The PyTorch demos (`demo-catastrophic-forgetting.py`, `demo-pruning.py`,
  `demo-quantization.py`) run on CPU with small models so the mechanism is
  visible and fast. In production the same techniques apply to full-size models.
- `demo-quantization.py` uses post-training dynamic quantization, which runs on
  CPU with no GPU or bitsandbytes. The 4-bit path used by QLoRA needs a CUDA GPU
  and stays a concept in this course.
