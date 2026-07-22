"""
Demo - Post-Training Dynamic Quantization
Day 3 - Session 4

Goal: Show that int8 quantization shrinks a model with a small accuracy cost.

We build a small PyTorch model of linear layers, apply dynamic quantization to
convert its Linear layers to int8, and print the on-disk byte size before and
after. Dynamic quantization runs on CPU and needs no GPU, TensorFlow, or
bitsandbytes. The 4-bit path used by QLoRA needs CUDA and is concept only.

Run: python3 day3/demos/demo-quantization.py
"""

import os
import tempfile

import torch
import torch.nn as nn


class SmallNet(nn.Module):
    """A small stack of linear layers, the part quantization targets."""

    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 128),
        )

    def forward(self, x):
        return self.net(x)


def disk_size_bytes(model):
    """Save the model state dict to a temp file and return its size in bytes."""
    path = os.path.join(tempfile.gettempdir(), "model_tmp.pt")
    torch.save(model.state_dict(), path)
    size = os.path.getsize(path)
    os.remove(path)
    return size


def select_quantized_engine():
    """Pick a CPU quantization backend that exists on this machine.

    fbgemm ships with x86 builds (Colab), qnnpack with ARM builds (Apple
    Silicon). Setting one avoids the "NoQEngine" error at inference time.
    """
    available = torch.backends.quantized.supported_engines
    for engine in ("fbgemm", "qnnpack"):
        if engine in available:
            torch.backends.quantized.engine = engine
            return engine
    return None


def main():
    torch.manual_seed(0)
    engine = select_quantized_engine()
    print(f"Quantization engine: {engine or 'none available'}\n")
    model = SmallNet().eval()

    quantized = torch.quantization.quantize_dynamic(
        model, {nn.Linear}, dtype=torch.qint8
    )

    before = disk_size_bytes(model)
    after = disk_size_bytes(quantized)

    print("Post-training dynamic quantization (float32 -> int8)")
    print(f"  Before: {before:>8,} bytes")
    print(f"  After:  {after:>8,} bytes")
    print(f"  Reduction: {100 * (1 - after / before):.1f}% smaller")

    sample = torch.randn(1, 512)
    with torch.no_grad():
        diff = (model(sample) - quantized(sample)).abs().max().item()
    print(f"\nMax output difference on one sample: {diff:.4f}")
    print("Smaller model, close outputs: the quantization tradeoff.")


if __name__ == "__main__":
    main()
