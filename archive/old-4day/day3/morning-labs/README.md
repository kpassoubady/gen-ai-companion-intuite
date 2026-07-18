# Morning Session: Multi-turn Chatbot

Welcome to the Day 3 Morning Session!

## Objective
1. **Lab 3.1: Multi-turn Chatbot with Memory** - Build a chatbot that remembers user name and preferences across turns by maintaining conversation history and applying a sliding window.

## Setup
Before you begin, make sure you have activated your Python virtual environment. If you haven't set up the environment yet, please follow the [Setup Instructions](../../../README.md) in the root of the repository.

## Instructions

We have provided boilerplate code in the `start/` directory. Your goal is to complete the `TODO` sections in each file.

### Lab 3.1: Multi-turn Chatbot (`lab3_1_multi_turn_chat.py`)
Build a chatbot that remembers user name and preferences across turns.
1. Navigate to the `start/` folder and open `lab3_1_multi_turn_chat.py`.
2. Complete the `TODO` sections to:
   - Define a clear purpose, persona, and scope in the system message.
   - Maintain conversation history across turns.
   - Remember the user's name when they introduce themselves.
   - Implement at least one context window management strategy (e.g., sliding window).
   - Support built-in commands like `/clear`, `/history`, `/summary`, and `/tokens`.
3. **Stretch goals:**
   - Extract user facts into a separate context dict.
   - Implement summarization-based context management instead of a naive sliding window.
   - Add persona switching with a `/persona` command.
4. Run the file: `python lab3_1_multi_turn_chat.py`

**Expected interaction:**
```text
💬 Multi-turn Chatbot — Lab 3.1
Commands: /clear, /history, /summary, /tokens, quit/exit
--------------------------------------------------

👤 You: Hi, I'm Alice!

🤖 Bot: Hello Alice! How can I help you today?
```

## Getting Stuck?
If you get stuck, check the `solution/` folder for the completed code!
