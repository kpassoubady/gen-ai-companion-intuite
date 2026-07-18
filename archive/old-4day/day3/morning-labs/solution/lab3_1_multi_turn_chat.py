"""
Lab 3.1 — Multi-turn Chatbot with Memory
Day 3 — Session 1

Goal: Build a chatbot that remembers user name and preferences across turns.

Requirements:
1. Define a clear purpose, persona, and scope in the system message
2. Maintain conversation history across turns
3. Remember the user's name when they introduce themselves
4. Implement at least one context window management strategy
5. Support commands: /clear, /history, /summary, /tokens

Stretch goals:
- Extract user facts into a separate context dict
- Implement summarization-based context management
- Add persona switching with a /persona command

Run: python3 day3/labs/lab3_1_multi_turn_chat.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import tiktoken
from shared import get_completion, show_config


SYSTEM_MESSAGE = {
    "role": "system",
    "content": """You are CodeBuddy, a friendly and patient programming assistant.

AUDIENCE: Developers of all skill levels
TONE: Encouraging, clear, uses code examples

CAPABILITIES:
- Answer programming questions in any language
- Explain concepts with examples
- Help debug code
- Remember user preferences shared during conversation

RULES:
- When the user shares their name, use it naturally in responses
- Adapt complexity to the user's stated skill level
- Keep responses under 200 words unless asked for more detail
- If unsure, say so honestly""",
}

MAX_TURNS = 20  # sliding window size (user+assistant pairs)


def count_tokens(messages, model="gpt-4o"):
    """Count total tokens in the conversation."""
    enc = tiktoken.encoding_for_model(model)
    total = 0
    for msg in messages:
        total += len(enc.encode(msg["content"]))
        total += 4  # overhead per message (role, separators)
    return total


def apply_sliding_window(conversation, max_turns=MAX_TURNS):
    """Keep system message + last N user/assistant pairs."""
    system = [conversation[0]]
    turns = conversation[1:]
    if len(turns) > max_turns * 2:
        turns = turns[-(max_turns * 2):]
    return system + turns


def summarize_history(conversation, keep_recent=6):
    """Summarize old messages, keep recent ones intact."""
    if len(conversation) <= keep_recent + 1:
        return conversation

    system = conversation[0]
    old_turns = conversation[1:-keep_recent]
    recent = conversation[-keep_recent:]

    old_text = "\n".join(f"{m['role']}: {m['content']}" for m in old_turns)
    summary = get_completion([
        {"role": "system", "content": "Summarize this conversation in 2-3 "
         "sentences. Preserve: user's name, preferences, key decisions."},
        {"role": "user", "content": old_text},
    ], temperature=0.0, max_tokens=200)

    return [system,
            {"role": "system", "content": f"Earlier conversation summary: {summary}"},
            *recent]


def show_history(conversation):
    """Display the current conversation history."""
    print(f"\n📜 Conversation History ({len(conversation)} messages):")
    for i, msg in enumerate(conversation):
        role = msg["role"]
        content = msg["content"][:80]
        suffix = "..." if len(msg["content"]) > 80 else ""
        print(f"  [{i}] {role:>10}: {content}{suffix}")


def main():
    show_config()
    print("\n💬 Multi-turn Chatbot — Lab 3.1")
    print("Commands: /clear, /history, /summary, /tokens, quit/exit")
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

        # Handle commands
        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        if user_input == "/clear":
            conversation = [SYSTEM_MESSAGE]
            print("🔄 Conversation cleared.")
            continue

        if user_input == "/history":
            show_history(conversation)
            continue

        if user_input == "/tokens":
            tokens = count_tokens(conversation)
            print(f"📊 Current tokens: ~{tokens}")
            print(f"   Messages: {len(conversation)}")
            continue

        if user_input == "/summary":
            conversation = summarize_history(conversation)
            print("📝 Conversation history summarized.")
            show_history(conversation)
            continue

        # Add user message
        conversation.append({"role": "user", "content": user_input})

        # Apply context window management
        conversation = apply_sliding_window(conversation)

        # Get response
        try:
            response = get_completion(conversation, tier="mini")
            print(f"\n🤖 Bot: {response}")

            # Add assistant response to history
            conversation.append({"role": "assistant", "content": response})

        except Exception as e:
            print(f"\n❌ Error: {e}")
            # Remove the failed user message
            conversation.pop()

    tokens = count_tokens(conversation)
    print(f"\n📊 Final stats: {len(conversation)} messages, ~{tokens} tokens")
    print("✅ Lab 3.1 complete!")


if __name__ == "__main__":
    main()
