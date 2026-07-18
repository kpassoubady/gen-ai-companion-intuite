# Lab 2.4 - Function Calling and a Simple Agent

**Day 2 - Session 4**

## Objectives

1. Define tools the model can call, each a typed function with a docstring.
2. Build a smolagents `CodeAgent` that chains the tools to answer a question.
3. Read the ReAct loop of thought, action, and observation in the agent log.

## Setup

Run in Google Colab (recommended): open `start/lab2_4_agent.ipynb` with the
"Open in Colab" badge and run the first cell to install dependencies.

This lab calls an LLM API through the shared client. Provide a key one of these
ways:

- **Colab:** add `OPENAI_API_KEY` as a Colab secret, or type it when prompted.
- **Local:** copy `.env.example` to `.env` and set your provider and key. See the
  [root README](../../README.md).

The agent uses the `mini` tier to keep cost low. Runs on CPU; no GPU needed.

## Instructions

1. Open `start/lab2_4_agent.ipynb`.
2. Fill in each `# TODO`: write the second tool, build the `CodeAgent`, and run
   it with a question that needs both tools.
3. Run every cell. The agent should call `get_tax_rate` then `calculate_total`
   and return about $268.12 for a $250 purchase in California.
4. Try the stretch goals: add a third tool, or rebuild the loop in LangGraph.

## Getting Stuck?

The full working code is in `solution/lab2_4_agent.ipynb`. It uses smolagents as
the primary path and includes a LangGraph version of the same agent as a stretch.
