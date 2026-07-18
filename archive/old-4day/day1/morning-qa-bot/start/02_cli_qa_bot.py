"""
Lab: CLI Q&A Script
Goal: Build an interactive command-line chatbot with conversation history.

Run: cd to this directory, then execute 'python 02_cli_qa_bot.py'
"""

import sys
sys.path.insert(0, "../../..")

from shared import get_completion_full, show_config

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a friendly and knowledgeable Python tutor. "
        "You explain concepts clearly with examples. "
        "Keep responses concise — under 200 words unless asked for detail."
    ),
}

def main():
    show_config()
    print("\n💬 CLI Q&A Bot — Type your question (or 'quit' to exit)")
    print("-" * 50)

    conversation = [SYSTEM_MESSAGE]

    while True:
        try:
            user_input = input("\n👤 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        # TODO: 1. Add the user message to conversation history
        # conversation.append({"role": "user", "content": user_input})

        # TODO: 2. Call get_completion_full with the conversation
        
        # TODO: 3. Extract the response content

        # TODO: 4. Add assistant response to conversation history so it remembers for next time
        
        # TODO: 5. Print the response
        
        print("⚠️  TODO: Implement the API calls!")

if __name__ == "__main__":
    main()
