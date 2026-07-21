# Day 3 Exercise - Adapting, Grounding, and Deploying

**Day 3 wrap-up** (self-paced, do it any time)

One short exercise that revisits everything from Day 3 in a single Colab notebook. You build it step by step. If you get stuck, ask your AI assistant (ChatGPT, Gemini, Claude, or the assistant in your editor) to write the code for each step, paste it into Colab, and run it.

You do not need to write code from scratch. Each part below has a ready-to-use prompt you can hand to an LLM.

## What you will practice

1. **Session 1:** fine-tune a small BERT model for classification.
2. **Session 2:** configure a LoRA adapter for parameter-efficient fine-tuning.
3. **Session 3:** build a local RAG pipeline with FAISS.
4. **Session 4:** apply dynamic int8 quantization to shrink a PyTorch model.

## Setup

1. Open [Google Colab](https://colab.research.google.com) and create a new notebook.
2. Keep the free CPU runtime.
3. Install anything a step needs with `!pip install ...` in the first cell.

## How to use an LLM for this

For each part, copy the prompt in the code block into your AI assistant, then copy its answer into a Colab cell and run it. If a cell errors, paste the error message back to the assistant and ask it to fix the code.

## The exercise

### Part 1: Fine-tuning DistilBERT

Run a short fine-tuning loop on a pre-trained model.

```text
Write Python for Google Colab that:
1. Installs transformers and datasets.
2. Loads 'distilbert-base-uncased' and its tokenizer.
3. Creates a tiny mock dataset with two sentences: "I love this" (label 1) and "I hate this" (label 0).
4. Tokenizes the dataset.
5. Uses the Hugging Face Trainer to train for 1 epoch with a small batch size.
6. Prints a success message when training completes.
```

**You should see:** the Trainer outputting a log table showing the loss after one epoch.

### Part 2: Parameter-Efficient Fine-Tuning (LoRA)

Attach a low-rank adapter to a frozen base model to save memory.

```text
Write Python for Google Colab that:
1. Installs peft and transformers.
2. Loads 'gpt2' as a base causal LM.
3. Creates a LoraConfig with rank 8 and alpha 16, targeting "c_attn".
4. Uses get_peft_model() to attach the LoRA adapter.
5. Prints the number of trainable parameters using print_trainable_parameters().
```

**You should see:** a printout proving that less than 1% of the model's total parameters are trainable.

### Part 3: Retrieval-Augmented Generation (RAG)

Embed chunks and retrieve the most relevant one using FAISS.

```text
Write Python for Google Colab that:
1. Installs faiss-cpu and sentence-transformers.
2. Loads the 'all-MiniLM-L6-v2' embedding model.
3. Embeds three short text chunks about taxes, pets, and cars.
4. Indexes the embeddings in a FAISS FlatL2 index.
5. Queries the index with "How do I file my W-2?"
6. Prints the text of the top 1 most relevant chunk.
```

**You should see:** the RAG retriever pulling the tax-related chunk and ignoring the pets and cars.

### Part 4: Deployment Optimization (Quantization)

Shrink a model's size on disk using int8 dynamic quantization.

```text
Write Python for Google Colab that:
1. Imports torch and torch.nn.
2. Defines a simple PyTorch model with three nn.Linear layers.
3. Instantiates the model.
4. Uses torch.quantization.quantize_dynamic to convert the nn.Linear layers to int8.
5. Prints the size of both models in memory (or saves them to temp files and prints their size in bytes).
```

**You should see:** the quantized model taking up significantly less space than the original float32 model.

## Success checklist

- [ ] Part 1 completes a training epoch using the Hugging Face Trainer
- [ ] Part 2 prints a trainable parameter count showing under 1%
- [ ] Part 3 retrieves the correct chunk using FAISS
- [ ] Part 4 prints a size comparison proving the quantized model is smaller

## Stretch goals

- In Part 1, change the base model to `roberta-base` and see if the code still works.
- In Part 2, change the LoRA rank to 32 and observe how the trainable parameter count increases.
- In Part 3, add a dummy LLM generation step that takes the retrieved chunk and inserts it into a prompt string.
- In Part 4, pass a random tensor through both models and verify the output differences are small.

## Getting stuck?

Each part maps to a lab or demo from today. Open the matching notebook or script for reference:

| Part | Reference lab / demo |
| :--- | :--- |
| Part 1 | [Lab 3.1](../lab3_1_bert_finetune/) |
| Part 2 | [Lab 3.2](../lab3_2_lora/) |
| Part 3 | [Lab 3.4](../lab3_4_rag/) |
| Part 4 | S4 Demo (`demo-quantization.py` in slides repo) |
