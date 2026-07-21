"""
Demo - The Function-Calling Loop
Day 2 - Session 4

Goal: Show the mechanics of function calling: the model requests a tool by name
with arguments, your code runs it, and the result goes back to the model.

We simulate the model with a small rule-based function so the loop runs offline
with no API key. Real providers return the same shape (a tool name plus JSON
arguments); only the "decide" step is done by the LLM instead of our stub.

No API key needed. No model download. Pure Python.

Run: python3 day2/demos/demo-function-calling.py
"""

import json

# 1. Tools your code exposes. The model only sees names, docs, and schemas.
TOOL_SCHEMA = [
    {"name": "get_weather", "description": "Current weather for a city.",
     "parameters": {"city": "string"}},
    {"name": "calculator", "description": "Evaluate a simple math expression.",
     "parameters": {"expression": "string"}},
]


def get_weather(city):
    fake = {"Paris": "18C and cloudy", "Austin": "33C and sunny"}
    return fake.get(city, "unknown")


def calculator(expression):
    return eval(expression, {"__builtins__": {}}, {})  # demo only: trusted input


TOOLS = {"get_weather": get_weather, "calculator": calculator}


def fake_model(user_message):
    """Stand-in for an LLM. Returns either a tool call or a final answer."""
    text = user_message.lower()
    if "weather" in text and "paris" in text:
        return {"type": "tool_call", "name": "get_weather",
                "arguments": {"city": "Paris"}}
    if "15" in text and "*" not in text:  # "15 percent tip on 40"
        return {"type": "tool_call", "name": "calculator",
                "arguments": {"expression": "40 * 0.15"}}
    return {"type": "final", "content": "I can help with weather or math."}


def run(user_message):
    print(f"\nUser: {user_message}")
    step = fake_model(user_message)

    if step["type"] == "tool_call":
        name, args = step["name"], step["arguments"]
        print(f"  Model requests tool: {name}({json.dumps(args)})")
        result = TOOLS[name](**args)
        print(f"  Your code runs it   -> {result}")
        print(f"  Result sent back to the model, which writes the final reply.")
        print(f"  Model: The answer is {result}.")
    else:
        print(f"  Model: {step['content']}")


def main():
    print("Function-calling loop: describe tools, model asks, you run, feed back.")
    print(f"\nTools exposed to the model:\n{json.dumps(TOOL_SCHEMA, indent=2)}")

    run("What is the weather in Paris?")
    run("What is a 15 percent tip on a 40 dollar bill?")

    print("\n\nTakeaway: the model never runs code. It only requests a call in a")
    print("structured format; your code decides what actually executes.")


if __name__ == "__main__":
    main()
