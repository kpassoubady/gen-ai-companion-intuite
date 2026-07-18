# Afternoon Session: Advanced Prompting & LLM Features

Welcome to the Day 2 Afternoon Session!

## Objective
1. **Lab 2.3: Temperature Experiment** - See how temperature affects output quality and creativity.
2. **Lab 2.4: Streaming Chat Loop** - Build a streaming chat bot that displays responses token-by-token.
3. **Lab 2.5: Refactor Assistant** - Build a tool that takes messy Python code and returns clean, refactored code with an explanation.
4. **Lab 2.6: Email Drafter** - Build a tool that takes bullet points and drafts a professional customer email with an explanation.

## Setup
Before you begin, make sure you have activated your Python virtual environment. If you haven't set up the environment yet, please follow the [Setup Instructions](../../README.md) in the root of the repository.

## Instructions

We have provided boilerplate code in the `start/` directory. Your goal is to complete the `TODO` sections in each file.

### Lab 2.3: Temperature Experiment (`lab2_3_temperature.py`)
See how temperature affects output quality and creativity.
1. Open `lab2_3_temperature.py` in the `start/` folder.
2. Complete the `TODO` sections to:
   - Pick a creative task: "Generate 5 marketing taglines for a coffee shop called Byte Brew that caters to software developers"
   - Run the same prompt at temperatures: 0.0, 0.2, 0.5, 0.7, 1.0, 1.2
   - Log all outputs side by side
   - Rate each set: creativity (1-5), relevance (1-5), coherence (1-5)
   - Find the "sweet spot" for this task
   - **Bonus:** Try the same experiment with `top_p` values: 0.3, 0.5, 0.7, 0.9, 1.0
3. Run the file: `python lab2_3_temperature.py`

### Lab 2.4: Streaming Chat Loop (`lab2_4_streaming_chat.py`)
Build a streaming chat bot that displays responses token-by-token.
1. Open `lab2_4_streaming_chat.py` in the `start/` folder.
2. Complete the `TODO` sections to:
   - Accept user input in a loop
   - Maintain conversation history
   - Stream responses to the terminal in real-time
   - Display total tokens used after each response
   - Support commands: `/clear`, `/temp 0.5` (change temperature)
   - **Stretch goals:** Add a typing indicator while waiting for the first token, measure and display time-to-first-token vs total generation time
3. Run the file: `python lab2_4_streaming_chat.py`

### Lab 2.5: Refactor Assistant (`lab2_5_refactor_assistant.py`)
Build a tool that takes messy Python code and returns clean, refactored code with an explanation. Iterate the prompt **3 times** based on observed failures.
1. Open `lab2_5_refactor_assistant.py` in the `start/` folder.
2. Complete the `TODO` sections to accept a Python code snippet and return refactored code + explanation of changes, maintaining original behavior (no functional changes), following PEP 8, adding type hints, improving naming.
3. **The iteration process:**
   - **v1:** Write your initial prompt. Test with 3 samples. Note failures.
   - **v2:** Fix the most common failure. Test again.
   - **v3:** Fix the next failure. Test again.
   - Document what changed and why at each iteration.
4. Run the file: `python lab2_5_refactor_assistant.py`

**Sample Input:**
```python
# Messy code to refactor
def proc(d):
    r = []
    for i in d:
        if i['status'] == 'active' and i['age'] > 18:
            n = i['first'] + ' ' + i['last']
            r.append({'name': n, 'email': i['email']})
    return r
```

**Expected output:** Clean version with descriptive names, type hints, docstring, and explanation of every change made.

### Lab 2.6: Email Drafter (`lab2_6_email_drafter.py`)
Build a tool that takes bullet points and returns a professional customer email. Iterate the prompt **3 times** based on observed failures.
1. Open `lab2_6_email_drafter.py` in the `start/` folder.
2. Complete the `TODO` sections to accept brief bullet points as input and return a professional, ready-to-send email. Iterate to fix tone, length, and missing call-to-actions, following business email conventions.
3. **The iteration process:**
   - **v1:** Write your initial prompt. Test with 3 samples. Note failures.
   - **v2:** Fix the most common failure. Test again.
   - **v3:** Fix the next failure. Test again.
   - Document what changed and why at each iteration.
4. Run the file: `python lab2_6_email_drafter.py`

**Sample Input:**
```text
- Customer: Acme Corp
- Issue: API rate limit exceeded
- Solution: Upgrade to Pro plan or optimize API calls
- Next step: Schedule a 15-min call to discuss
```

**Expected output:** A clear, empathetic professional email structured with a greeting, acknowledgment, solution, and clear next steps, kept under 150 words.

## Getting Stuck?
If you get stuck, check the `solution/` folder for the completed code!
