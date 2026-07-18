"""
Demo: Conversation Context Management
Day 3 — Session 1

Shows three scenarios:
1. Without history — the model forgets everything
2. With history — the model remembers across turns
3. Context overflow — what happens when history grows too large

Run: python3 day3/demos/demo-conversation-context.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import tiktoken
from shared import get_completion, show_config


def count_tokens(messages, model="gpt-4o"):
    """Count total tokens in a conversation."""
    enc = tiktoken.encoding_for_model(model)
    total = 0
    for msg in messages:
        total += len(enc.encode(msg["content"]))
    return total


def demo_without_history():
    """Show that separate API calls have no memory."""
    print("\n" + "=" * 60)
    print("📌 Demo 1: WITHOUT conversation history")
    print("   Each call is independent — no memory")
    print("=" * 60)

    # Call 1
    messages1 = [{"role": "user", "content": "My name is Alice and I work at Acme Corp."}]
    response1 = get_completion(messages1, tier="mini")
    print(f"\n👤 User: My name is Alice and I work at Acme Corp.")
    print(f"🤖 Bot:  {response1}")

    # Call 2 — completely separate, no history
    messages2 = [{"role": "user", "content": "What's my name and where do I work?"}]
    response2 = get_completion(messages2, tier="mini")
    print(f"\n👤 User: What's my name and where do I work?")
    print(f"🤖 Bot:  {response2}")
    print(f"\n❌ The model doesn't know — each call starts fresh!")


def demo_with_history():
    """Show that maintaining history enables memory."""
    print("\n" + "=" * 60)
    print("📌 Demo 2: WITH conversation history")
    print("   Full conversation sent with each request")
    print("=" * 60)

    conversation = [
        {"role": "system", "content": "You are a helpful assistant. Be concise."},
    ]

    exchanges = [
        "My name is Alice and I work at Acme Corp.",
        "What's my name and where do I work?",
        "I prefer Python over JavaScript.",
        "What programming language do I prefer?",
    ]

    for user_input in exchanges:
        conversation.append({"role": "user", "content": user_input})
        response = get_completion(conversation, tier="mini")
        conversation.append({"role": "assistant", "content": response})

        tokens = count_tokens(conversation)
        print(f"\n👤 User: {user_input}")
        print(f"🤖 Bot:  {response}")
        print(f"   📊 Conversation: {len(conversation)} messages, ~{tokens} tokens")

    print(f"\n✅ The model remembers everything because we send full history!")


def demo_sliding_window():
    """Show sliding window strategy for managing long conversations."""
    print("\n" + "=" * 60)
    print("📌 Demo 3: Sliding window context management")
    print("   Keep only the last N turns to manage token usage")
    print("=" * 60)

    system = {"role": "system", "content": "You are a helpful math tutor. Be concise."}
    conversation = [system]

    # Simulate a longer conversation
    questions = [
        "What is 2 + 2?",
        "Multiply that by 3.",
        "Now subtract 5.",
        "What's the square root of the result?",
        "Round that to 2 decimal places.",
        "Is that number prime?",
        "What's the next prime number after it?",
        "Multiply the original answer (from question 1) by 10.",
    ]

    window_size = 4  # keep last 4 messages (2 turns)

    for i, question in enumerate(questions):
        conversation.append({"role": "user", "content": question})

        # Apply sliding window
        if len(conversation) > 1 + window_size * 2:
            windowed = [system] + conversation[-(window_size * 2):]
            label = f"windowed ({len(windowed)} msgs)"
        else:
            windowed = conversation
            label = f"full ({len(windowed)} msgs)"

        response = get_completion(windowed, tier="mini", temperature=0.0)
        conversation.append({"role": "assistant", "content": response})

        tokens = count_tokens(windowed)
        print(f"\n👤 Q{i+1}: {question}")
        print(f"🤖 Bot:  {response}")
        print(f"   📊 Sent: {label}, ~{tokens} tokens")

    print(f"\n⚠️  Notice: Q8 asks about Q1's answer, but the sliding window may have")
    print(f"   dropped that context. This is the tradeoff with windowing!")


def main():
    show_config()
    print("\n🔄 Demo: Conversation Context Management")

    demo_without_history()
    input("\n⏎  Press Enter for the next demo...")

    demo_with_history()
    input("\n⏎  Press Enter for the next demo...")

    demo_sliding_window()

    print("\n" + "=" * 60)
    print("📊 Summary:")
    print("   1. Without history: model has zero memory")
    print("   2. With history: model remembers everything you send")
    print("   3. Sliding window: bounded cost, but may lose old context")
    print("=" * 60)
    print("\n✅ Demo complete!")


if __name__ == "__main__":
    main()
