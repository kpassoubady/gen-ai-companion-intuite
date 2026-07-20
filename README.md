# Gen AI Labs Companion

Welcome to the Gen AI course! This repository contains the hands-on labs you will complete during the workshops. Every lab is a Jupyter notebook, organized by day and session.

## How to run the labs

You have three ways to run each lab. **Use Google Colab first** whenever you can. It needs no local install, runs the GPU labs for free, and every notebook is already set up to work there. If you prefer to stay in your editor, run the notebooks in VS Code against Colab compute (Option 2). Run fully locally only if you prefer your own machine or have no internet in class (Option 3).

### Option 1: Google Colab (recommended)

1. Open the notebook you want. Each `start/` notebook has an **Open In Colab** badge at the top: click it to launch the lab in Colab.
2. (Optional) **Fork** this repo to your own GitHub account first if you want to save your edits back to GitHub. Clicking the badge alone still lets you run and save a copy to your Google Drive (`File -> Save a copy in Drive`).
3. Run the cells top to bottom. The first cell installs the packages the lab needs.
4. For labs that call an LLM, add your API key as a Colab secret:
   - Click the key icon in the left sidebar (**Secrets**).
   - Add a secret named `OPENAI_API_KEY` (or `GEMINI_API_KEY` / `ANTHROPIC_API_KEY`) with your key as the value, and enable notebook access.
   - The setup cell reads it automatically. If no secret is found, it prompts you to paste the key once.

Colab notebooks that use the shared LLM client clone this repo automatically, so there is nothing else to set up.

### Option 2: VS Code with the Colab extension

Run notebooks inside VS Code while still using Colab's compute (including the free GPU). This keeps your editor but avoids a heavy local install.

1. Install **VS Code**.
2. Install the **Colab** extension (by Google) from the Visual Studio Marketplace or the Open VSX registry.
3. Open or create a notebook file (`.ipynb`), for example `day1/lab1_1_classifier/start/lab1_1_classifier.ipynb`.
4. When prompted, sign in to your Google account.
5. Click **Select Kernel** in the top right, then choose **Colab -> Auto Connect**.
6. Run the cells. Add your LLM API key as a Colab secret the same way as in Option 1.

### Option 3: Local machine

1. **Clone this repository** to your local machine.
2. **Create a virtual environment**:

   **Mac / Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up API keys** (needed for the LLM labs in Day 2 and Day 3):
   - Copy `.env.example` to `.env`.
   - Fill in your API keys in the `.env` file.
5. **Open the notebooks** in VS Code or Jupyter:
   ```bash
   jupyter lab
   ```
   Then open a `start/` notebook, for example `day1/lab1_1_classifier/start/lab1_1_classifier.ipynb`, and run the cells.

The GPU labs (image classification, VAE, diffusion, fine-tuning, LoRA) run much faster on Colab's free GPU. On a CPU-only laptop they still run but can be slow.

## Exercise structure

For each session you will find two folders:
- `start/`: the notebook with `TODO` markers. This is where you write your code.
- `solution/`: the fully working reference notebook. Open it if you get stuck.

## How the shared client works on Colab

Some labs (the LLM ones in Day 2, Day 3, and the capstone) import a helper called `get_completion` from the `shared/` package. When you open a notebook in Colab, Colab loads only that single `.ipynb` file, so the `shared/` folder is not there at first.

You do not need to clone or copy anything by hand. The setup cell near the top of those notebooks handles it for you:
- It looks for a local `shared/` folder (used when you run locally).
- On Colab, it finds none, so it runs `git clone` on this repo into the session and adds it to the Python path. `from shared import ...` then works.

A few things to know:
- The clone lands in the temporary Colab VM, not your Google Drive. Nothing is saved to Drive, and it re-clones automatically the next time the runtime starts.
- This only works because the repo is public. Just run the cells top to bottom.
- The Day 1 labs and a few others are self-contained and do not use `shared/`, so they never clone.

## Lab index

| Day | Lab | Folder |
| :--- | :--- | :--- |
| Day 1 | Train and evaluate a classifier | `day1/lab1_1_classifier/` |
| Day 1 | Image classification | `day1/lab1_2_image_clf/` |
| Day 1 | Variational autoencoder | `day1/lab1_3_vae/` |
| Day 1 | Diffusion pipeline | `day1/lab1_4_diffusion/` |
| Day 2 | Similarity search | `day2/lab2_1_similarity/` |
| Day 2 | BERT and GPT | `day2/lab2_2_bert_gpt/` |
| Day 2 | Prompting techniques | `day2/lab2_3_prompting/` |
| Day 2 | Simple agent | `day2/lab2_4_agent/` |
| Day 3 | BERT fine-tuning | `day3/lab3_1_bert_finetune/` |
| Day 3 | LoRA | `day3/lab3_2_lora/` |
| Day 3 | Sampling techniques | `day3/lab3_3_sampling/` |
| Day 3 | End-to-end RAG | `day3/lab3_4_rag/` |
| Capstone | Capstone project | `capstone/` |

Follow the instructions in the `README.md` file inside each session's folder for lab-specific details.

## Why VS Code helps you learn faster

Running the labs in VS Code (Option 2 or 3) has one big advantage over the browser: you can use your AI coding assistant right inside the notebook. Tools like GitHub Copilot, Claude, Cline, or the Continue extension can read the `# TODO` markers and the surrounding code and suggest a working solution, explain an error, or walk you through the concept.

A few ways to use them well:
- Ask the assistant to explain what a cell does before you fill in a `TODO`, so you understand the code instead of just pasting it.
- When a cell errors, paste the traceback and ask what went wrong and how to fix it.
- After you get a lab working, ask the assistant to review your solution or try one of the stretch goals.

Treat the assistant as a tutor, not an autopilot. The goal is to understand each lab, and the `solution/` notebook is always there to check your answer.
