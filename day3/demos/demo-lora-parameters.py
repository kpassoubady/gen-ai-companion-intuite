"""
Demo - LoRA Parameter Math
Day 3 - Session 2

Goal: Show why LoRA trains so few parameters and how a low-rank B x A update
approximates a full-size weight change.

Part 1 counts parameters: a full weight matrix W is d x k, while LoRA learns two
small matrices B (d x r) and A (r x k). For a small rank r the trainable count
drops by a large factor. Part 2 builds a real weight update, factors it with an
SVD-based rank-r approximation, and shows the reconstruction error shrinks as r
grows. That is the same idea LoRA relies on.

No API key, no downloads. Pure NumPy on CPU.

Run: python3 day3/demos/demo-lora-parameters.py
"""

import numpy as np

np.random.seed(0)


def count_parameters():
    """Compare full-matrix parameters against LoRA B x A parameters."""
    print("1. Parameter count: full matrix vs LoRA adapter\n")
    d, k = 4096, 4096  # a typical attention projection shape
    full = d * k
    print(f"  Weight matrix W: {d} x {k} = {full:,} parameters")
    print(f"  {'rank r':>8}  {'LoRA params (B x A)':>20}  {'% of full':>10}")
    for r in (4, 8, 16, 64):
        lora = d * r + r * k  # B is d x r, A is r x k
        print(f"  {r:>8}  {lora:>20,}  {100 * lora / full:>9.2f}%")
    print("\n  A small rank trains a tiny fraction of the full weight count.")


def low_rank_approximation():
    """Show a rank-r B x A approximates a full weight update."""
    print("\n2. How well a rank-r update approximates a full change\n")
    d, k = 64, 64
    delta_w = np.random.randn(d, k)  # the "ideal" full-fine-tune weight update
    u, s, vt = np.linalg.svd(delta_w)
    total_energy = np.sum(s)

    print(f"  Target update DeltaW: {d} x {k}")
    print(f"  {'rank r':>8}  {'reconstruction error':>22}  {'energy kept':>12}")
    for r in (1, 4, 8, 32, 64):
        # Best rank-r factorization: B = U[:, :r] * S[:r], A = Vt[:r]
        b = u[:, :r] * s[:r]
        a = vt[:r]
        approx = b @ a
        error = np.linalg.norm(delta_w - approx) / np.linalg.norm(delta_w)
        kept = np.sum(s[:r]) / total_energy
        print(f"  {r:>8}  {error:>22.3f}  {kept:>11.1%}")

    print("\n  Higher rank captures more of the update at the cost of more params.")


def main():
    print("LoRA freezes W and learns a low-rank B x A update instead.\n")
    count_parameters()
    low_rank_approximation()
    print("\nTakeaway: low rank captures most of a weight change for few parameters.")


if __name__ == "__main__":
    main()
