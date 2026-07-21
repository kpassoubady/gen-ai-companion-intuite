# Day 2 Labs - Advanced NLP, Pre-trained Models & Agentic AI

Hands-on labs for Day 2. Each lab has a `start/` notebook with `# TODO` markers
and a `solution/` notebook with the full working code. Every lab runs on a Google
Colab CPU runtime with no GPU required.

| Lab | Topic | Session | API key |
| :--- | :--- | :--- | :--- |
| [Lab 2.1](lab2_1_similarity/) | Find similar documents with embeddings | Session 1 | No |
| [Lab 2.2](lab2_2_bert_gpt/) | Introduction to BERT and GPT | Session 2 | No |
| [Lab 2.3](lab2_3_prompting/) | Prompting techniques and generative tasks | Session 3 | Yes |
| [Lab 2.3 (no key)](lab2_3_prompting_nokey/) | Same techniques on a local model | Session 3 | No |
| [Lab 2.4](lab2_4_agent/) | Function calling and a simple agent | Session 4 | Yes |
| [Lab 2.4 (no key)](lab2_4_agent_nokey/) | Same agent loop in pure Python | Session 4 | No |

## How to run

Open a lab's `start/` notebook with its "Open in Colab" badge and run the first
cell to install that lab's dependencies. Work through the `# TODO` markers. The
matching `solution/` notebook has the reference answer.

Labs 2.1 and 2.2 run fully offline with local models (sentence-transformers and
small Hugging Face models). Labs 2.3 and 2.4 call an LLM API through the shared
client, so set an API key in Colab secrets or your local `.env` first. If you do
not have a key, run the no-key versions of 2.3 and 2.4 instead: they teach the
same ideas with a small local model and pure Python, no key required.

To run locally instead, see the [root README](../README.md) for environment
setup.
