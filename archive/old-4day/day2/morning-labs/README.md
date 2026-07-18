# Morning Session: Prompt Engineering Labs

Welcome to the Day 2 Morning Session!

## Objective
1. **Lab 2.1: Sentiment Classifier** - Build a sentiment classifier, first with zero-shot, then improve with few-shot.
2. **Lab 2.2: Resume Parser** - Parse unstructured resume text into structured JSON.

## Setup
Before you begin, make sure you have activated your Python virtual environment. If you haven't set up the environment yet, please follow the [Setup Instructions](../../README.md) in the root of the repository.

## Instructions

We have provided boilerplate code in the `start/` directory. Your goal is to complete the `TODO` sections in each file.

### Lab 2.1: Sentiment Classifier (`lab2_1_sentiment.py`)
Build a sentiment classifier, first with zero-shot, then improve with few-shot.
1. Navigate to the `start/` folder and open `lab2_1_sentiment.py`.
2. Find the `TODO` comments.
3. Build a zero-shot sentiment classifier (POSITIVE / NEGATIVE / NEUTRAL).
4. Test it on 10 sample texts, note where it fails.
5. Add 3-5 few-shot examples to improve accuracy.
6. Compare results: zero-shot vs few-shot.
7. Bonus: Add a confidence score to the output.
8. Run the file: `python lab2_1_sentiment.py`

### Lab 2.2: Resume Parser (`lab2_2_resume_parser.py`)
Parse unstructured resume text into structured JSON.
1. Open `lab2_2_resume_parser.py` in the `start/` folder.
2. Complete the `TODO` sections to:
   - Write a system prompt that extracts: name, email, phone, skills, experience, education.
   - Force JSON output (prompt-based or JSON mode).
   - Parse the JSON response with `json.loads()`.
   - Handle edge cases: missing fields, malformed JSON.
   - Test with 3 different resume formats.
3. Run the file: `python lab2_2_resume_parser.py`

**Expected output:**
```json
{
    "name": "Sarah Chen",
    "email": "sarah@example.com",
    "skills": ["Python", "Django", "PostgreSQL"],
    "experience_years": 5,
    "education": "BS Computer Science, MIT"
}
```

## Getting Stuck?
If you get stuck, check the `solution/` folder for the completed code!
