"""
Lab 1.2 — CLI Q&A Script
Day 1 — Session 2

Goal: Build an interactive command-line chatbot with conversation history.

Requirements:
1. Accept user input from the terminal in a loop
2. Maintain conversation history (multi-turn)
3. Include a system message that sets the persona
4. Display token usage after each response
5. Type 'quit' or 'exit' to end

Stretch goals:
- /clear  — reset conversation history
- /tokens — show total tokens used so far
- /model  — switch between default and mini tier

Run: cd to this directory, then execute 'python 02_cli_qa_bot.py'
"""

import sys
sys.path.insert(0, "../../..")

from shared import get_completion_full, show_config

# System message — customize this!
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
    print("Commands: /clear, /tokens, /model")
    print("-" * 50)

    conversation = [SYSTEM_MESSAGE]
    total_tokens = 0
    current_tier = "mini"

    while True:
        try:
            user_input = input("\n👤 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        # Handle commands
        if user_input.lower() in ("quit", "exit"):
            print(f"\nTotal tokens used: {total_tokens}")
            print("Goodbye!")
            break

        if user_input == "/clear":
            conversation = [SYSTEM_MESSAGE]
            total_tokens = 0
            print("🔄 Conversation cleared.")
            continue

        if user_input == "/tokens":
            print(f"📊 Total tokens used so far: {total_tokens}")
            print(f"   Messages in history: {len(conversation)}")
            continue

        if user_input == "/model":
            current_tier = "default" if current_tier == "mini" else "mini"
            print(f"🔄 Switched to tier: {current_tier}")
            continue

        conversation.append({"role": "user", "content": user_input})

        response = get_completion_full(
            messages=conversation,
            tier=current_tier,
        )

        content = response.choices[0].message.content
        usage = response.usage

        conversation.append({"role": "assistant", "content": content})

        total_tokens += usage.total_tokens

        print(f"\n🤖 Bot: {content}")
        print(f"   [{usage.prompt_tokens} + {usage.completion_tokens} = "
              f"{usage.total_tokens} tokens | tier={current_tier}]")


if __name__ == "__main__":
    main()
