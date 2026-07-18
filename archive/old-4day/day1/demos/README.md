# Instructor Demos: Day 1

This folder contains instructor-led demonstration scripts that can be run directly from the terminal to show students important Gen AI concepts in action.

## Setup

Before running the demos, ensure that your virtual environment is activated and your API keys are configured in the root of the repository.

```bash
# 1. Activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your API keys
cp .env.example .env
```

To run these scripts, navigate to this specific directory in your terminal:

```bash
cd day1/demos
```

## Available Demos

### 1. Tokenizer Visualizer
This demo uses the official OpenAI `tiktoken` library to break down how text is translated into the integer tokens that LLMs actually process.

**Run the script:**
```bash
python demo-tokenizer.py
```

**What it demonstrates:**
- **Model Differences:** How `gpt-4o` tokenization differs from older models.
- **Languages & Code:** How English is highly optimized compared to other languages like Japanese, and how Python/JSON is tokenized.
- **Cost Estimation:** Calculates the exact API cost for a given string based on the token count.
- **Edge Cases:** Shows how leading spaces, capitalization, and emojis affect token boundaries.

---

### 2. Model Comparison
This demo sends the exact same prompt to two different model tiers (e.g., `gpt-4o-mini` vs `gpt-4o`) so students can visually compare the speed, cost, and qualitative depth of the responses.

**Run the script:**
```bash
python demo-model-comparison.py
```

**What it demonstrates:**
- **Quality Differences:** The "default" tier will typically provide a deeper, more nuanced explanation of the CAP theorem compared to the "mini" tier.
- **Token Usage:** Shows the exact prompt and completion token counts returned by the API.
- **Cost vs Performance:** Great for discussing when to use a cheaper, faster model versus a more capable, expensive one.
