"""
Lab 2.4 — Streaming Chat Loop
Day 2 — Session 3

Goal: Build a streaming chat bot that displays responses token-by-token.

Requirements:
1. Accept user input in a loop
2. Maintain conversation history
3. Stream responses to the terminal in real-time
4. Display total tokens used after each response
5. Support commands: /clear, /temp <value>

Stretch goals:
- Add a typing indicator while waiting for the first token
- Measure and display time-to-first-token vs total generation time

Run: python3 day2/labs/lab2_4_streaming_chat.py
"""

import sys
import time

import os

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import litellm
from shared import get_model, show_config


SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a helpful and knowledgeable programming assistant. "
        "You explain concepts clearly with concise examples. "
        "Keep responses focused and under 300 words unless asked for detail."
    ),
}


def stream_response(messages, tier="mini", temperature=0.7):
    """Stream a response from the LLM, printing tokens as they arrive."""

    model = get_model(tier)
    start_time = time.time()
    first_token_time = None
    full_response = ""
    
    response = litellm.completion(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=1024,
        stream=True,
    )
    
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            if first_token_time is None:
                first_token_time = time.time()
            print(delta, end="", flush=True)
            full_response += delta
    
    print()  # newline
    end_time = time.time()
    
    ttft = (first_token_time - start_time) if first_token_time else 0
    total = end_time - start_time
    print(f"   [TTFT: {ttft:.2f}s | Total: {total:.2f}s]")
    
    return full_response



def main():
    show_config()
    print("\n🌊 Streaming Chat — Lab 2.4")
    print("Commands: /clear, /temp <value>, quit/exit")
    print("-" * 50)

    conversation = [SYSTEM_MESSAGE]
    current_temp = 0.7
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
            print("Goodbye!")
            break

        if user_input == "/clear":
            conversation = [SYSTEM_MESSAGE]
            print("🔄 Conversation cleared.")
            continue

        if user_input.startswith("/temp"):
            parts = user_input.split()
            if len(parts) == 2:
                try:
                    new_temp = float(parts[1])
                    if 0.0 <= new_temp <= 2.0:
                        current_temp = new_temp
                        print(f"🌡️  Temperature set to {current_temp}")
                    else:
                        print("⚠️  Temperature must be between 0.0 and 2.0")
                except ValueError:
                    print("⚠️  Usage: /temp 0.7")
            else:
                print(f"🌡️  Current temperature: {current_temp}")
            continue

        # Add user message
        conversation.append({"role": "user", "content": user_input})

        # Stream the response
        print("\n🤖 Bot: ", end="", flush=True)
        response_text = stream_response(
            conversation, tier=current_tier, temperature=current_temp
        )

        # Add to conversation history
        if response_text:
            conversation.append({"role": "assistant", "content": response_text})


if __name__ == "__main__":
    main()
