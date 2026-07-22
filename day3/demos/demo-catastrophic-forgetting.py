"""
Demo - Catastrophic Forgetting
Day 3 - Session 1

Goal: Show that training a model hard on a new task can erase what it learned on
an earlier task.

We build one small neural net and two tasks over the same 2D input space. Task A
and Task B use different decision boundaries. We train on Task A first and measure
its accuracy, then train only on Task B and measure both again. Task B accuracy
climbs while Task A accuracy collapses: the weights that solved A were overwritten.

No API key, no downloads. Pure PyTorch on CPU.

Run: python3 day3/demos/demo-catastrophic-forgetting.py
"""

import torch
import torch.nn as nn

torch.manual_seed(0)


def make_task(boundary):
    """Return (X, y): label 1 when x0 + x1 > boundary, else 0."""
    x = torch.rand(400, 2) * 2 - 1  # points in [-1, 1] x [-1, 1]
    y = (x[:, 0] + x[:, 1] > boundary).long()
    return x, y


def accuracy(model, x, y):
    """Fraction of correct predictions."""
    with torch.no_grad():
        preds = model(x).argmax(dim=1)
    return (preds == y).float().mean().item()


def train(model, x, y, steps=300):
    """Train the model to convergence on one task."""
    opt = torch.optim.Adam(model.parameters(), lr=0.05)
    loss_fn = nn.CrossEntropyLoss()
    for _ in range(steps):
        opt.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        opt.step()


def main():
    print("Catastrophic forgetting: learn Task B, lose Task A.\n")

    task_a = make_task(boundary=0.5)
    task_b = make_task(boundary=-0.5)

    model = nn.Sequential(nn.Linear(2, 16), nn.ReLU(), nn.Linear(16, 2))

    train(model, *task_a)
    a_after_a = accuracy(model, *task_a)
    print("After training on Task A only:")
    print(f"  Task A accuracy: {a_after_a:.2f}")

    train(model, *task_b)
    a_after_b = accuracy(model, *task_a)
    b_after_b = accuracy(model, *task_b)
    print("\nAfter then training on Task B only:")
    print(f"  Task A accuracy: {a_after_b:.2f}  (dropped from {a_after_a:.2f})")
    print(f"  Task B accuracy: {b_after_b:.2f}")

    print("\nTakeaway: narrow, hard fine-tuning overwrites earlier skills.")
    print("Lower the learning rate, use fewer epochs, or prefer PEFT to reduce it.")


if __name__ == "__main__":
    main()
