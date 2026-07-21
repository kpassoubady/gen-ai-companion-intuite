"""
Demo - A ReAct Agent (Thought, Action, Observation)
Day 2 - Session 4

Goal: Show the ReAct loop where a model interleaves reasoning and tool use over
several steps to reach a goal, using the TurboTax scenario from the slides.

The agent must answer "How much tax do I owe on my W-2 wages?" It cannot do this
in one shot: it fetches the W-2 (Action 1), sums the wages with a calculator
(Action 2), then answers. We script the reasoning so the trace is deterministic
and runs offline; a real agent lets the LLM produce each Thought/Action.

No API key needed. No model download. Pure Python.

Run: python3 day2/demos/demo-react-agent.py
"""

# Tools the agent can call.
W2_FORMS = {"user_42": {"employer": "Acme", "box1_wages": 68000, "box2_withheld": 9200}}


def fetch_w2(user_id):
    return W2_FORMS.get(user_id, {})


def calculator(expression):
    return eval(expression, {"__builtins__": {}}, {})  # demo only: trusted input


TOOLS = {"fetch_w2": fetch_w2, "calculator": calculator}

# Scripted plan: (thought, tool_name, argument). A real agent gets these from
# the LLM one step at a time, reading each observation before the next thought.
PLAN = [
    ("I need the user's W-2 before I can compute anything.", "fetch_w2", "user_42"),
    ("I have wages of 68000. Estimate tax at a flat 22 percent.",
     "calculator", "68000 * 0.22"),
]


def run_agent(goal, max_steps=5):
    print(f"Goal: {goal}\n")
    observations = []
    for i, (thought, tool, arg) in enumerate(PLAN[:max_steps], start=1):
        print(f"Step {i}")
        print(f"  Thought    : {thought}")
        print(f"  Action     : {tool}({arg!r})")
        observation = TOOLS[tool](arg)
        print(f"  Observation: {observation}")
        observations.append(observation)

    wages = observations[0]["box1_wages"]
    tax = observations[1]
    print("\nFinal answer:")
    print(f"  On W-2 wages of ${wages:,}, estimated tax is ${tax:,.0f} "
          "(flat 22% estimate).")


def main():
    print("ReAct = Reason + Act. Think, call a tool, observe, repeat until done.\n")
    run_agent("How much tax do I owe on my W-2 wages?")
    print("\nTakeaway: the loop keeps the model honest by grounding each step in")
    print("real tool output instead of guessing the whole answer at once.")


if __name__ == "__main__":
    main()
