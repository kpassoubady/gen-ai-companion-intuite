# PEFT, LoRA, and Quantization

Reference for parameter-efficient fine-tuning, the LoRA low-rank adapter idea, QLoRA and 4-bit quantization as concepts, and rank and alpha guidance.

---

## Why PEFT

Full fine-tuning updates every weight in the model. For a large model this needs GPU memory for the weights, gradients, and optimizer state, and it produces a full-size checkpoint for every task. Parameter-efficient fine-tuning (PEFT) freezes the base model and trains a small set of new parameters instead.

- Far less GPU memory, since gradients and optimizer state cover only the small trained set.
- Small checkpoints (megabytes, not gigabytes) that you can swap per task.
- The frozen base keeps its general ability, which reduces catastrophic forgetting.

## LoRA: Low-Rank Adapters

LoRA (Low-Rank Adaptation) freezes the original weight matrix `W` and learns a small update expressed as the product of two low-rank matrices `B` and `A`. Instead of learning a full-size change to `W`, LoRA learns `B x A` where the inner dimension `r` (the rank) is small.

```
output = W·x + (B·A)·x
```

`W` has shape `d x d`. `A` has shape `r x d` and `B` has shape `d x r`, with `r` much smaller than `d`. Only `A` and `B` are trained, so the number of trainable parameters drops from `d x d` to `2 x d x r`. At inference you add the low-rank update back onto the frozen weights.

### LoRA with the peft library

```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
)
model = get_peft_model(base_model, config)
model.print_trainable_parameters()  # often < 1% of total
```

You then train `model` with the normal `Trainer` loop. Saving produces a small adapter that loads on top of the original base model later.

## Rank and Alpha Guidance

| Setting | What it does | Typical values |
| :--- | :--- | :--- |
| **r (rank)** | Capacity of the adapter | 4 to 16 for small tasks, up to 64 for harder ones |
| **lora_alpha** | Scales the adapter update | Often 2x the rank |
| **lora_dropout** | Regularization on the adapter | 0.0 to 0.1 |
| **target_modules** | Which layers get adapters | Attention projections (`q_proj`, `v_proj`) are common |

Start with a small rank. Raise it only if the model underfits the task. A larger rank adds capacity and trainable parameters but can overfit small datasets.

## QLoRA and 4-bit Quantization (Concept Only)

Quantization stores weights with fewer bits (for example 4-bit integers instead of 16-bit floats), which shrinks memory use. QLoRA loads the frozen base model in 4-bit and trains LoRA adapters on top, so you can fine-tune a large model on a single smaller GPU.

This is concept only in this course. The `bitsandbytes` 4-bit path needs a CUDA GPU and does not run on CPU or Apple Silicon, so the labs use plain LoRA on a small model. The idea to remember: quantize the frozen base to save memory, keep the small adapter in higher precision for training.
