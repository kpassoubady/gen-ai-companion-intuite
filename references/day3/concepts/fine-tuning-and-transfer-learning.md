# Fine-Tuning and Transfer Learning

Reference for transfer learning, feature extraction versus full fine-tuning, when to fine-tune, cost, catastrophic forgetting, and the Hugging Face Trainer workflow.

---

## Transfer Learning

Transfer learning starts from a model already trained on a large general dataset and adapts it to a new task with a small amount of task-specific data. The base model already encodes useful language or vision features, so you reuse that knowledge instead of learning it again.

Training a model from scratch needs a huge dataset and large compute budget. Transfer learning reaches good accuracy with far less data and time because most of the useful representation is already in the base weights.

## Feature Extraction vs Full Fine-Tuning

There are two common ways to adapt a pre-trained model.

- **Feature extraction:** freeze the pre-trained backbone and train only a new task head (for example a classification layer). Fast, cheap, and low risk, but the model cannot adjust its internal features.
- **Full fine-tuning:** update all weights, backbone and head together. Higher accuracy on the target task, at the cost of more compute, more memory, and more risk of overfitting.

| Aspect | Feature extraction | Full fine-tuning |
| :--- | :--- | :--- |
| Weights updated | New head only | All weights |
| Compute and memory | Low | High |
| Data needed | Small | Larger |
| Overfitting risk | Low | Higher |
| Best when | Task close to pre-training | Task needs deeper adaptation |

## When to Fine-Tune

Fine-tuning fits a fixed style, format, or narrow task that prompting alone cannot reach reliably. Reach for it when you have labeled examples and the behavior you want is stable over time.

- Prompt engineering first: no training, immediate, cheap to iterate.
- Retrieval-augmented generation next: use it when the model needs private or changing facts.
- Fine-tuning last: use it for a consistent style, format, or task where you have labeled data and the target behavior does not change often.

## Cost Considerations

Full fine-tuning of a large model requires GPUs with enough memory to hold the model, gradients, and optimizer state, which is often several times the model size. Each fine-tuned copy is a full-size checkpoint to store and serve. These costs are the reason parameter-efficient methods like LoRA exist (see `peft-lora-quantization.md`).

## Catastrophic Forgetting

Catastrophic forgetting is when a model loses general ability after being trained too hard on a narrow task. Task accuracy climbs while the model gets worse at everything else.

Mitigations:

- Use a lower learning rate so weights move less.
- Train for fewer epochs and watch a validation set.
- Use parameter-efficient fine-tuning (PEFT) so the base weights stay frozen.
- Mix in some general examples alongside the task data.

## Hugging Face Trainer Workflow

The `transformers` library provides a `Trainer` that handles the training loop, batching, and evaluation. A typical text-classification fine-tune looks like this.

```python
from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                          Trainer, TrainingArguments)

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding="max_length")

train_ds = dataset["train"].map(tokenize, batched=True)

args = TrainingArguments(output_dir="out", num_train_epochs=1,
                         per_device_train_batch_size=8, learning_rate=2e-5)
trainer = Trainer(model=model, args=args, train_dataset=train_ds)
trainer.train()
```

The same pattern applies to other tasks by swapping the model class (for example `AutoModelForSeq2SeqLM` for summarization) and the dataset.

## Summarization as Fine-Tuning

Summarization uses a sequence-to-sequence model such as T5 (Text-to-Text Transfer Transformer, which frames every task as text in and text out) or BART (Bidirectional and Auto-Regressive Transformers, a denoising encoder-decoder). The workflow is the same as classification: load a pre-trained seq2seq model, tokenize document and reference-summary pairs, and train with `Trainer` (or `Seq2SeqTrainer`). In practice, prompting a capable instruction-tuned model handles most summarization without any training, so fine-tune only when you need a specific summary style or length that prompting cannot hold.
