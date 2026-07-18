# Morning Session: Building a QA Bot

Welcome to the Day 1 Morning Session! In this exercise, you will learn the basics of calling Large Language Models and building an interactive command-line Chatbot.

## Objective

1. **Part 1: Hello LLM** - Learn how to interact with the LLM for one-shot NLP tasks (Summarization, Classification, Translation, etc.).
2. **Part 2: CLI QA Bot** - Build an interactive, multi-turn chatbot that remembers conversation history.

## Setup

Before you begin, make sure you have activated your Python virtual environment. If you haven't set up the environment yet, please follow the [Setup Instructions](../../README.md) in the root of the repository.

## Instructions

We have provided boilerplate code in the `start/` directory. Your goal is to complete the `TODO` sections in each file.

### Part 1: Hello LLM (`01_hello_llm.py`)
This script contains 5 common NLP tasks.
1. Navigate to the `start/` folder and open `01_hello_llm.py`.
2. Find the `TODO` comments.
3. Use the `get_completion_full` function imported from `shared` to complete the tasks. You will need to construct the appropriate `messages` array containing a `system` prompt and a `user` prompt for each task.
4. Run the file: `python 01_hello_llm.py`
5. Try passing different models (e.g. `tier="mini"`) to see how output quality changes!

### Part 2: CLI QA Bot (`02_cli_qa_bot.py`)
This script sets up a loop to take input from the command line.
1. Open `02_cli_qa_bot.py` in the `start/` folder.
2. Complete the `TODO` sections to:
   - Append the user's input to the `conversation` history list.
   - Send the full conversation to the LLM.
   - Extract the `content` and `usage` statistics.
   - Append the LLM's response back into the conversation history so it has context for the next question.
3. Run the file: `python 02_cli_qa_bot.py`

## Getting Stuck?
If you get stuck, check the `solution/` folder for the completed code!
