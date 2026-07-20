"""
Demo - Gradient Descent
Day 1 - Session 2

Goal: Show how gradient descent lowers a loss step by step.

We minimize a simple loss, f(w) = (w - 3)^2, starting from a random weight.
At each step we compute the gradient (the slope) and take a small step
downhill. Watch the loss drop and the weight move toward the minimum at w = 3.

Run: python3 day1/demos/demo-gradient-descent.py
"""

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def loss(w):
    return (w - 3) ** 2


def gradient(w):
    return 2 * (w - 3)


def descend(start=-4.0, learning_rate=0.1, steps=30):
    """Run gradient descent and record the path."""
    w = start
    history = [(w, loss(w))]
    for _ in range(steps):
        w = w - learning_rate * gradient(w)
        history.append((w, loss(w)))
    return history


def main():
    history = descend()
    for i, (w, l) in enumerate(history):
        if i % 5 == 0 or i == len(history) - 1:
            print(f"step {i:2d}:  w = {w:6.3f}   loss = {l:7.4f}")

    weights = [w for w, _ in history]
    losses = [l for _, l in history]

    output = os.path.join(os.path.dirname(__file__), "gradient-descent.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    grid = [(-5 + 0.1 * i) for i in range(120)]
    ax1.plot(grid, [loss(w) for w in grid], color="#1a73e8", label="loss curve")
    ax1.scatter(weights, losses, color="#e65100", s=18, zorder=3, label="steps")
    ax1.set_title("Stepping downhill on the loss")
    ax1.set_xlabel("weight w")
    ax1.set_ylabel("loss")
    ax1.legend()

    ax2.plot(range(len(losses)), losses, color="#2e7d32", marker="o", markersize=3)
    ax2.set_title("Loss over training steps")
    ax2.set_xlabel("step")
    ax2.set_ylabel("loss")

    fig.tight_layout()
    fig.savefig(output, dpi=120)
    print(f"Saved figure to {output}")


if __name__ == "__main__":
    main()
