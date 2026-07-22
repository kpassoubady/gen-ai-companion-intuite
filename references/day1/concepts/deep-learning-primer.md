# Deep Learning Primer

Reference for neural networks: what they are made of, how they learn, and the frameworks used to build them.

---

## What Deep Learning Is

Deep learning uses neural networks with many layers to learn features directly from raw data. Classic machine learning relies on a human to design features; deep learning learns the features and the mapping together. That is why it works so well on images, audio, and text.

Deep learning usually needs more data than classic machine learning before it pays off. On small tabular datasets, tree-based models often win.

## The Neuron

A single neuron does three things:

1. Multiplies each input by a weight.
2. Adds a bias.
3. Applies an activation function to the result.

Written out, a neuron computes `activation(w · x + b)`. A network is many of these neurons arranged in layers.

## Layers

A network has an input layer, one or more hidden layers, and an output layer. Each connection has a weight, and training adjusts all of these weights.

## Activation Functions

Without a non-linear activation, stacking layers collapses into a single linear function. Non-linearity is what lets networks model complex patterns.

- **ReLU:** the default for hidden layers, fast and simple.
- **Sigmoid:** squashes values to 0-1, used for probabilities.
- **Softmax:** turns a vector of scores into a probability distribution over classes.

## Common Architectures

| Architecture | Best at | Example |
| :--- | :--- | :--- |
| **Feedforward (MLP)** | Tabular, simple tasks | Credit scoring |
| **CNN** | Grid data like images | Digit recognition |
| **RNN / LSTM** | Sequences | Older text models |
| **Transformer** | Sequences at scale | Modern LLMs |

## How a Network Learns

Training repeats a loop:

1. **Forward pass:** run inputs through the network to get predictions.
2. **Loss:** measure how wrong the predictions are with a single number.
3. **Backpropagation:** compute the gradient of the loss for every weight.
4. **Update:** the optimizer nudges the weights to lower the loss.

### Loss Functions

- **Cross-entropy** for classification.
- **Mean squared error** for regression.

### Learning Rate and Optimizers

The learning rate sets how big each update step is. Too big and training diverges; too small and it crawls. SGD is the baseline optimizer. Adam adapts the step size per weight and is a common default.

Backpropagation is the algorithm that computes the gradients efficiently by applying the chain rule backward through the network.

## Frameworks

| | PyTorch | TensorFlow |
| :--- | :--- | :--- |
| Feel | Pythonic, flexible | Strong production tooling |
| Deployment | TorchServe, ExecuTorch | TF Serving, TF Lite |
| In this course | Primary | Shown as an option |

Both frameworks build the same networks. This course uses PyTorch for the labs.

## A Minimal PyTorch Model

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
)
```

The training loop then fills in the weights so the model classifies images correctly.
