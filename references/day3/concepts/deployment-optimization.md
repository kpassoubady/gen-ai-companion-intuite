# Deployment Optimization

Reference for shrinking and speeding up models before deployment: quantization, pruning, and distillation, with tradeoffs and guidance on when to use each.

---

## Why Optimize

A trained model is often larger and slower than a deployment needs. Optimization reduces model size, memory use, and latency so it fits the target hardware and cost budget, usually with a small accuracy cost. The three common techniques are quantization, pruning, and distillation, and they can be combined.

## Quantization

Quantization stores weights and sometimes activations with fewer bits, for example 8-bit integers instead of 32-bit floats. Smaller numbers mean less memory and faster arithmetic.

- **Post-training quantization:** convert a trained model after the fact. Fast to apply, small accuracy cost.
- **Quantization-aware training:** simulate low precision during training so the model adapts. More work, better accuracy at very low bit widths.

Dynamic quantization to int8 runs on CPU and is a good demonstration. The 4-bit path used by QLoRA needs a CUDA GPU, so it is concept only here.

## Pruning

Pruning removes weights that contribute little to the output, setting them to zero or deleting whole structures.

- **Unstructured pruning:** zero out individual small weights. High sparsity, but needs sparse-aware hardware to speed up.
- **Structured pruning:** remove whole neurons, channels, or attention heads. Gives real speedups on standard hardware.

After pruning, a short fine-tune often recovers most of the lost accuracy.

## Distillation

Knowledge distillation trains a small student model to imitate a large teacher model. The student learns from the teacher's output distributions rather than only hard labels, which transfers more information than training the small model alone. DistilBERT is a distilled version of BERT that keeps most of the accuracy at a fraction of the size.

## Tradeoffs

| Technique | Size | Latency | Accuracy cost | Retrain needed |
| :--- | :--- | :--- | :--- | :--- |
| **Quantization** | Much smaller | Lower | Small | No (post-training) |
| **Pruning** | Smaller | Lower (structured) | Small to moderate | Often a short fine-tune |
| **Distillation** | Much smaller | Much lower | Moderate | Yes, train the student |

## When to Use Each

- Reach for quantization first: it is the cheapest to apply and often enough on its own.
- Add structured pruning when you need more speedup on standard hardware.
- Use distillation when you can afford to train and want a permanently smaller model to serve.

These techniques stack. A common recipe is to distill to a smaller architecture, then quantize the student for deployment.
