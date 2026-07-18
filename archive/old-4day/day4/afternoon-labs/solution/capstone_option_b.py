import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI()

# Mock documentation for RAG
DOCS = {
    "auth.md": "User authentication is handled via JWT tokens. Tokens expire after 1 hour. Pass the token in the Authorization header as 'Bearer <token>'.",
    "deploy.md": "Deployments are triggered automatically when code is pushed to the 'main' branch. It takes approximately 5 minutes for a deployment to complete.",
    "api.md": "The API rate limit is 100 requests per minute per user. If you exceed this, you will receive a 429 Too Many Requests response."
}

SYSTEM_PROMPT = """You are a documentation assistant for the project.
Answer questions based ONLY on the retrieved documentation below.
Always cite sources using [Source: filename].
If the docs don't cover the topic, say so clearly: 'I cannot answer this based on the available documentation.'

Retrieved Documentation:
{context}"""

def chat(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"API Error: {e}"

def evaluate_assistant():
    context = ""
    for filename, content in DOCS.items():
        context += f"\n--- {filename} ---\n{content}\n"
    
    test_cases = [
        {
            "question": "How do I authenticate?",
            "expected_source": "[Source: auth.md]"
        },
        {
            "question": "What is the capital of France?",
            "expected_source": "I cannot answer this"
        }
    ]
    
    print("--- Running Evaluation ---")
    for test in test_cases:
        print(f"\nEvaluating: {test['question']}")
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT.format(context=context)},
            {"role": "user", "content": test['question']}
        ]
        result = chat(messages)
        passed = test['expected_source'].lower() in result.lower()
        print(f"Passed: {passed}")
    print("--- Evaluation Complete ---\n")

def main():
    print("Documentation Q&A Bot (Option B)")
    
    # Run evaluation
    evaluate_assistant()
    
    print("Interactive Mode:")
    context = ""
    for filename, content in DOCS.items():
        context += f"\n--- {filename} ---\n{content}\n"
        
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT.format(context=context)}
    ]
    
    while True:
        user_input = input("\nAsk a question (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
            
        messages.append({"role": "user", "content": user_input})
        
        response = chat(messages)
        print(f"\nAssistant: {response}")
        
        # Add assistant response to history to maintain multi-turn context
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
