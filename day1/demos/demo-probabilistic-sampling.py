"""
Demo - Probabilistic Sampling
Day 1 - Session 3

Goal: Show that generation is sampling from a learned distribution.

We fit a simple distribution to a small 2D dataset, then draw new samples
from it. The new points are not copies of the originals, yet they follow the
same pattern. This is the core idea behind every generative model.

Run: python3 day1/demos/demo-probabilistic-sampling.py
"""

import os

import matplotlib
import numpy as np

matplotlib.use("Agg")  # render to a file so the demo runs anywhere
import matplotlib.pyplot as plt

OUTPUT = os.path.join(os.path.dirname(__file__), "probabilistic-sampling.png")


def make_original_data(n=300, seed=0):
    """Create a small 2D dataset shaped like two blobs."""
    rng = np.random.default_rng(seed)
    blob_a = rng.normal(loc=[-2, -1], scale=[0.6, 0.4], size=(n // 2, 2))
    blob_b = rng.normal(loc=[2, 1], scale=[0.5, 0.7], size=(n // 2, 2))
    return np.vstack([blob_a, blob_b])


def fit_distribution(data):
    """Fit a Gaussian to the data by estimating its mean and covariance."""
    mean = data.mean(axis=0)
    cov = np.cov(data, rowvar=False)
    return mean, cov


def sample_new_points(mean, cov, n=300, seed=1):
    """Draw brand-new points from the fitted distribution."""
    rng = np.random.default_rng(seed)
    return rng.multivariate_normal(mean, cov, size=n)


def main():
    data = make_original_data()
    mean, cov = fit_distribution(data)
    samples = sample_new_points(mean, cov)

    print("Fitted mean:", np.round(mean, 3))
    print("Fitted covariance:\n", np.round(cov, 3))
    print(f"Drew {len(samples)} brand-new samples from the fitted distribution.")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), sharex=True, sharey=True)
    ax1.scatter(data[:, 0], data[:, 1], s=12, color="#1a73e8")
    ax1.set_title("Original data")
    ax2.scatter(samples[:, 0], samples[:, 1], s=12, color="#2e7d32")
    ax2.set_title("New samples")
    for ax in (ax1, ax2):
        ax.set_aspect("equal")
    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=120)
    print(f"Saved figure to {OUTPUT}")


if __name__ == "__main__":
    main()
