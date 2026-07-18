"""
Lab 2.2 — Resume Parser with JSON Output
Day 2 — Session 2

Goal: Parse unstructured resume text into structured JSON.

Instructions:
1. Write a system prompt that extracts: name, email, phone, skills,
   experience_years, education
2. Force JSON output (prompt-based or JSON mode)
3. Parse the JSON response with json.loads()
4. Handle edge cases: missing fields, malformed JSON
5. Test with the 3 sample resumes below

Run: python3 day2/labs/lab2_2_resume_parser.py
"""

import sys
import json

import os

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from shared import get_completion, show_config


SYSTEM_MESSAGE = """You are a resume parsing assistant. Extract structured information from resume text.

Respond with ONLY valid JSON (no markdown fences, no explanation outside JSON):

{
    "name": "full name",
    "email": "email address or null",
    "phone": "phone number or null",
    "skills": ["skill1", "skill2", ...],
    "experience_years": number or null,
    "education": "highest degree and school or null",
    "current_role": "current/most recent job title or null",
    "current_company": "current/most recent company or null"
}

Rules:
- If a field is not found in the text, set it to null (for strings/numbers) or [] (for arrays)
- For experience_years, calculate from the earliest to latest date mentioned
- For skills, include programming languages, frameworks, tools, and methodologies
- Do not invent information that is not in the text"""

# Sample resumes to parse
SAMPLE_RESUMES = [
    {
        "name": "Structured Resume",
        "text": """
Sarah Chen
Email: sarah.chen@email.com | Phone: (555) 123-4567

EXPERIENCE
Senior Software Engineer, TechCorp (2020 - Present)
- Led migration from monolithic to microservices architecture
- Built real-time data pipeline processing 1M events/day
- Mentored 4 junior developers

Software Engineer, StartupXYZ (2017 - 2020)
- Developed REST APIs using Python/Django
- Implemented CI/CD with GitHub Actions

EDUCATION
BS Computer Science, MIT (2017)

SKILLS
Python, Django, FastAPI, PostgreSQL, Redis, Docker, Kubernetes, AWS, Terraform
""",
    },
    {
        "name": "Informal Resume",
        "text": """
Hey! I'm Alex Rivera. I've been coding for about 8 years now, mostly in
JavaScript and TypeScript. Currently working at BigTech as a frontend lead
where I manage a team of 6 engineers building React applications.

Before that I was at a startup called CodeFlow where I built their entire
frontend from scratch using Next.js. I also know my way around Node.js,
GraphQL, and have dabbled in Python for data scripts.

I graduated from UC Berkeley with a degree in EECS back in 2016.

You can reach me at alex.rivera@gmail.com.
""",
    },
    {
        "name": "Minimal Resume",
        "text": """
DevOps Engineer
5 years experience with cloud infrastructure.
AWS, GCP, Docker, Kubernetes, Terraform, Ansible.
Certified AWS Solutions Architect.
Looking for remote opportunities.
""",
    },
]


def parse_resume(resume_text):
    """Send resume text to LLM for structured extraction."""
    # TODO: Implement this function
    # 1. Create messages with SYSTEM_MESSAGE and the resume text
    # 2. Call get_completion with temperature=0.0
    # 3. Parse the JSON response
    # 4. Handle malformed JSON gracefully

    return {"error": "TODO: Implement the parse_resume function!"}


def validate_result(result):
    """Check that the parsed result has all required fields."""
    required_fields = ["name", "email", "phone", "skills",
                       "experience_years", "education"]
    missing = [f for f in required_fields if f not in result]
    if missing:
        print(f"  ⚠️  Missing fields: {missing}")
    else:
        print(f"  ✅ All required fields present")

    # Check types
    if "skills" in result and not isinstance(result.get("skills"), list):
        print(f"  ⚠️  'skills' should be a list, got {type(result['skills']).__name__}")


def main():
    show_config()
    print("\n📄 Resume Parser — Lab 2.2")
    print("=" * 60)

    for resume in SAMPLE_RESUMES:
        print(f"\n📋 Parsing: {resume['name']}")
        print(f"{'─'*40}")
        print(f"Input (first 200 chars):\n{resume['text'][:200]}...")
        print(f"{'─'*40}")

        result = parse_resume(resume["text"])

        print(f"\nParsed Result:")
        print(json.dumps(result, indent=2))

        if "error" not in result:
            validate_result(result)

        print(f"{'='*60}")

    print("\n✅ Lab 2.2 complete!")


if __name__ == "__main__":
    main()
