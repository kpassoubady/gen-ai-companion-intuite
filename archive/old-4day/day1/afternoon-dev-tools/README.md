# Afternoon Session: AI Developer Tools

Welcome to the Day 1 Afternoon Session! In this exercise, you will build useful developer tools powered by LLMs.

## Objective

1. **Part 1: Code Explainer** - Build a tool that takes a Python code snippet and returns a plain-English explanation of its purpose, logic, and complexity.
2. **Part 2: Bug Triager** - Build a tool that accepts an error log, classifies its severity, and outputs structured JSON.
3. **Part 3: User Story Generator** - Build a tool that takes a brief feature idea and generates a structured Agile user story with acceptance criteria.

## Setup

Before you begin, make sure you have activated your Python virtual environment. If you haven't set up the environment yet, please follow the [Setup Instructions](../../README.md) in the root of the repository.

## Instructions

Boilerplate code is provided in the `start/` directory.

### Part 1: Code Explainer (`01_code_explainer.py`)
1. Navigate to the `start/` folder and open `01_code_explainer.py`.
2. Locate the `explain_code` function.
3. Construct the `messages` list using the provided `SYSTEM_MESSAGE` and the user's code snippet.
4. Call `get_completion` (note: for coding/explanation tasks, a low temperature like `0.3` is often best).
5. Run the file: `python 01_code_explainer.py` to see the generated Markdown explanations of the sample algorithms!

### Part 2: Bug Triager (`02_bug_triager.py`)
1. Open `02_bug_triager.py` in the `start/` folder.
2. Locate the `triage_error` function.
3. Construct the messages to prompt the LLM to output pure JSON according to the schema in the `SYSTEM_MESSAGE`.
4. Call `get_completion`. Since we want strict JSON output and no creative variation, pass `temperature=0.0`.
5. Parse the returned JSON string into a Python dictionary.
6. Run the file: `python 02_bug_triager.py` and review the output!

### Part 3: User Story Generator (`03_user_story.py`)
1. Open `03_user_story.py` in the `start/` folder.
2. Locate the `generate_user_story` function.
3. Construct the `messages` list using the `system_message` and the user's `feature_idea`.
4. Call `get_completion` (note: for generating structured content with slight creativity, a temperature like `0.3` is often best).
5. Run the file: `python 03_user_story.py` to interact with the generator in your terminal!

## Getting Stuck?
If you get stuck, check the `solution/` folder for the completed code!
