# Day 4 Afternoon Session: Evaluation and Capstone

## Objectives
1. Build an Evaluation Harness (Lab 4.3)
2. Build Your Own AI-Powered Developer Assistant (Capstone)

## Setup
Before running these scripts, ensure your Python environment is activated and your `OPENAI_API_KEY` is set in your `.env` file. See the [Setup Instructions](../../../README.md) for more details.

## Instructions

### Lab 4.3: Evaluation Harness
**Goal:** Build a script that runs test prompts, compares outputs to expected results, and logs pass/fail status based on keywords.

1. Navigate to the `start/` directory.
2. Open `lab4_3_eval_harness.py`.
3. Follow the `TODO` comments to implement an evaluation harness that scores LLM responses against expected keywords and forbidden terms.
4. Run the script: 
   ```bash
   python lab4_3_eval_harness.py
   ```

### Capstone Project: Build Your Own Assistant
**Goal:** Build your own AI-powered assistant. Choose one of the three options:
- **Option A**: Code Review Assistant (RAG over coding standards + prompt engineering)
- **Option B**: Documentation Q&A Bot (RAG + conversation context + source citation)
- **Option C**: Bug-Report Triager (Classification + structured output + eval)

1. Open `capstone.py` in the `start/` directory.
2. Design your system message for your chosen option in `SYSTEM_PROMPT`.
3. Implement the core API call to process the user input.
4. Add error handling and at least 5 test cases to evaluate your assistant.
5. Run your assistant and verify it works interactively:
   ```bash
   python capstone.py
   ```

## Getting Stuck?
Check the `solution/` directory for a complete, working reference implementation of the evaluation harness, as well as examples for all three capstone options.
