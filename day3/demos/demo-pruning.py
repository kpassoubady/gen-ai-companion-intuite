"""
Demo - Magnitude Pruning
Day 3 - Session 4

Goal: Show that removing the smallest-magnitude weights (pruning) makes a model
sparse with only a small change to its outputs.

We build a small PyTorch model, apply unstructured magnitude pruning to its
Linear layers so a fraction of the smallest weights become zero, and report the
resulting sparsity. We then compare outputs before and after on one input to see
how little the predictions move. Sparse weights compress well and can run faster
on hardware that skips zeros.

No API key, no downloads. Pure PyTorch on CPU.

Run: python3 day3/demos/demo-pruning.py
"""

import torch
import torch.nn as nn
import torch.nn.utils.prune as prune

torch.manual_seed(0)


class SmallNet(nn.Module):
    """A small stack of linear layers, the part pruning targets."""

    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 64),
        )

    def forward(self, x):
        return self.net(x)


def global_sparsity(model):
    """Fraction of weights across all Linear layers that are zero."""
    zeros, total = 0, 0
    for module in model.modules():
        if isinstance(module, nn.Linear):
            zeros += int(torch.sum(module.weight == 0))
            total += module.weight.nelement()
    return zeros / total


def main():
    print("Magnitude pruning: zero the smallest weights, keep the outputs close.\n")
    model = SmallNet().eval()
    sample = torch.randn(1, 256)
    with torch.no_grad():
        before_out = model(sample)

    print(f"Sparsity before pruning: {global_sparsity(model):.1%}")

    amount = 0.5  # prune 50% of the smallest-magnitude weights per layer
    for module in model.modules():
        if isinstance(module, nn.Linear):
            prune.l1_unstructured(module, name="weight", amount=amount)
            prune.remove(module, "weight")  # make the pruning permanent

    print(f"Sparsity after pruning {amount:.0%}: {global_sparsity(model):.1%}")

    with torch.no_grad():
        after_out = model(sample)
    diff = (before_out - after_out).abs().max().item()
    print(f"\nMax output difference on one sample: {diff:.4f}")
    print("Half the weights are zero, outputs stay close: the pruning tradeoff.")


if __name__ == "__main__":
    main()
