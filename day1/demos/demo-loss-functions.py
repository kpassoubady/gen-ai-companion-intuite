"""
Demo - Loss Functions
Day 1 - Session 2

Goal: Build intuition for the two most common loss functions.

Mean squared error (MSE) is used for regression: it grows with the squared
distance between the prediction and the target. Cross-entropy is used for
classification: it punishes a confident wrong answer sharply.

Run: python3 day1/demos/demo-loss-functions.py
"""

import math
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def mse(prediction, target):
    return (prediction - target) ** 2


def binary_cross_entropy(prob, label):
    """Loss when the true label is `label` (0 or 1) and we predicted `prob`."""
    eps = 1e-9  # keep the log finite at the edges
    prob = min(max(prob, eps), 1 - eps)
    return -(label * math.log(prob) + (1 - label) * math.log(1 - prob))


def main():
    target = 1.0
    preds = [(-2 + 0.05 * i) for i in range(120)]
    mse_values = [mse(p, target) for p in preds]

    probs = [0.001 * i for i in range(1, 1000)]
    ce_values = [binary_cross_entropy(p, label=1) for p in probs]

    print("MSE at prediction 1.0 (target 1.0):", round(mse(1.0, 1.0), 4))
    print("MSE at prediction 0.0 (target 1.0):", round(mse(0.0, 1.0), 4))
    print("Cross-entropy at prob 0.9 (label 1):", round(binary_cross_entropy(0.9, 1), 4))
    print("Cross-entropy at prob 0.1 (label 1):", round(binary_cross_entropy(0.1, 1), 4))

    output = os.path.join(os.path.dirname(__file__), "loss-functions.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(preds, mse_values, color="#1a73e8")
    ax1.axvline(target, color="#e65100", linestyle="--", label="target")
    ax1.set_title("MSE (regression), target = 1.0")
    ax1.set_xlabel("prediction")
    ax1.set_ylabel("loss")
    ax1.legend()

    ax2.plot(probs, ce_values, color="#2e7d32")
    ax2.set_title("Cross-entropy (classification), true label = 1")
    ax2.set_xlabel("predicted probability of label 1")
    ax2.set_ylabel("loss")

    fig.tight_layout()
    fig.savefig(output, dpi=120)
    print(f"Saved figure to {output}")


if __name__ == "__main__":
    main()
