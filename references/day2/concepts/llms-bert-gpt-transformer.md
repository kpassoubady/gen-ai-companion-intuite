# Large Language Models: BERT, GPT, and the Transformer

Reference for pre-trained language models: why pre-training matters, how encoders and decoders differ, and what the Transformer does at a high level.

---

## Before Pre-trained Models

Earlier NLP built features by hand and trained a separate model per task and per language, limited by small labeled datasets. Recurrent networks read text one word at a time, which was slow and forgot long-range context.

Pre-training changed the workflow. Train once on huge unlabeled text to learn language broadly, then reuse that model for many tasks with little or no extra data. Fine-tuning and prompting replaced building from scratch. This is transfer learning for language, the foundation of the Day 3 fine-tuning session.

## BERT vs GPT

Both are built from the Transformer. The difference is the direction attention is allowed to look and what the model is trained to do.

| | BERT (encoder) | GPT (decoder) |
| :--- | :--- | :--- |
| **Direction** | Both ways at once | Left to right |
| **Trained to** | Fill in masked words | Predict the next token |
| **Best for** | Understanding: classify, extract, search | Generation: write, complete, chat |

BERT reads the whole sentence and builds a rich understanding of each token in context. GPT reads what came before and predicts the next token, which makes it a natural fit for chat and writing.

## The Transformer

The Transformer processes a whole sequence at once and is built from repeated blocks of self-attention and feed-forward layers.

- **Self-attention** lets each token look at every other token and decide what matters, so long-range links are direct rather than passed word by word.
- **Feed-forward layers** process each token after attention mixes information across the sequence.
- **Token and position embeddings** give the model both the meaning and the order of tokens.

The architecture won because it is parallel (a whole sequence at once, unlike RNNs), it scales (more data and parameters keep helping), and it is general (the same block works for text, code, images, and audio).

## Autoregressive Generation

A decoder generates text by repeated next-token prediction. The model outputs a probability for every possible next token, picks one, appends it to the input, and repeats. Generation is nothing more mysterious than this loop.

## The Modern Landscape

- **Closed API models:** GPT-4o, Claude, Gemini, called over an API.
- **Open-weight models:** Llama, Qwen, Mistral, downloaded and run locally.
- **Reasoning models:** trained to think through hard problems step by step.
- **Multimodal models:** handle text plus images, audio, or video.

Most production use starts with an API call that sends messages and receives a completion. This course routes those calls through a shared client so switching providers needs no code changes.

## Hugging Face

Hugging Face is the hub for open models, datasets, and live demos (Spaces). The `transformers` library loads any hub model in a few lines, and the `pipeline` helper handles tokenizing, running the model, and decoding the output.

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("I love this course!"))
# [{'label': 'POSITIVE', 'score': 0.99}]
```
