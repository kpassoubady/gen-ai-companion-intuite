import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# TODO: Step 1 - Choose your option (A, B, or C) and design your system prompt.
# - Option A: Code Review Assistant
# - Option B: Documentation Q&A Bot
# - Option C: Bug-Report Triager
SYSTEM_PROMPT = """
"""

def process_input(user_input):
    """
    TODO: Step 3 - Implement the core functionality
    Make an API call to the LLM using your system prompt and the user input.
    Handle errors gracefully.
    """
    pass

def evaluate_assistant():
    """
    TODO: Step 4 - Add at least 5 test cases and a simple evaluation loop
    Define an array of test scenarios, run them through process_input,
    and print whether the results matched expectations.
    """
    print("Running evaluation...")
    pass

def main():
    print("Welcome to your AI-Powered Developer Assistant!")
    
    # Optional: Run evaluation on startup
    # evaluate_assistant()
    
    # Interactive loop
    while True:
        user_input = input("\nEnter your prompt (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        # Uncomment below when fully implemented
        # result = process_input(user_input)
        # print(f"\nAssistant Response:\n{result}")

if __name__ == "__main__":
    main()
