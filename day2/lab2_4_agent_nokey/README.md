# Lab 2.4 (No Key) - Function Calling and a ReAct Agent

**Day 2 - Session 4**

This is the no-key version of [Lab 2.4](../lab2_4_agent/). Use it if you do not
have an LLM API key. It teaches the same function-calling and ReAct loop.

## How this runs without an API key

This lab replaces the LLM with a small scripted planner (`plan_next_step`) so
the function-calling and ReAct loop are fully visible and deterministic. It is
pure Python: no installs, no key, no downloads. In the API lab the model
performs the planning step; the surrounding loop of request a tool, run it, and
feed the result back is identical.

## Objectives

1. Define tools the agent can call, each a plain typed function.
2. Register the tools and read the scripted planner that requests them.
3. Complete the ReAct loop: run each requested tool and feed the observation
   back until the goal is met.

## Setup

Run in Google Colab (recommended): open `start/lab2_4_agent_nokey.ipynb` with
the "Open in Colab" badge. There is nothing to install and no API key. It runs
instantly on any runtime.

## Instructions

1. Open `start/lab2_4_agent_nokey.ipynb`.
2. Fill in each `# TODO`: write the `calculate_total` tool and the tool-execution
   step inside `run_agent`.
3. Run every cell. The loop should print two steps (get_tax_rate then
   calculate_total) and a final answer of about $268.12 for a $250 purchase in
   California.
4. Try the stretch goals: add a tool and extend the planner, or add guardrails
   that validate arguments and reject unknown tools.

## Getting Stuck?

The full working code is in `solution/lab2_4_agent_nokey.ipynb`.
