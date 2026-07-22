# Agentic AI

Reference for tool use, function calling, the ReAct pattern, agent frameworks, and the Model Context Protocol.

---

## Why Tools

An LLM on its own cannot reliably do exact arithmetic on large numbers, look up current or private data, or take an action in another system. Tools let the model call your code to fill these gaps.

## Function Calling

You describe functions to the model with a name, a description, and a parameter schema. The model decides when to call one and returns the function name plus arguments in a structured format. Your code runs the function and passes the result back.

The model never runs code itself. It only requests a call, so you stay in control of what actually executes.

```python
def get_weather(city: str) -> str:
    """Return the current weather for a city."""
    ...
```

A clear name and docstring help the model decide when to call the tool and what arguments to pass.

### The Loop

1. The user sends a request.
2. The model either answers directly or returns a tool call.
3. Your code runs the tool and returns the result to the model.
4. The model uses the result to answer or to call another tool.

## From Function Calls to Agents

A single function call handles one step. An agent chains many: it breaks a goal into steps, picks and calls tools as needed, reads results, decides what to do next, and stops when the goal is met. The model drives the loop instead of you hard-coding each step.

## The ReAct Pattern

ReAct interleaves reasoning and acting in a loop: thought (reason about the next step), action (call a tool), observation (read the result), then repeat until the goal is met.

- Thought makes the plan explicit and easier to debug.
- Action uses tools for facts and computation.
- Observation grounds the next step in real results.

The loop keeps the model honest by checking against tool output each round.

## Agent Frameworks

Frameworks handle the loop, tool wiring, and output parsing so you focus on the task.

| Framework | Style |
| :--- | :--- |
| **smolagents** | Minimal, code-first agents |
| **LangGraph** | Graph of steps and state |
| **LlamaIndex** | Data and retrieval focused |

Lab 2.4 uses a single smolagents `CodeAgent`, with LangGraph offered as a stretch goal.

## Keeping Agents Safe

Agents take actions, so guardrails matter. Limit which tools an agent can use, cap the number of steps to avoid runaway loops, validate arguments before running a tool, and log every action for review. Give an agent the least power it needs to do the job.

## Model Context Protocol (MCP)

Without a standard, every tool needs custom wiring for every app. MCP defines one protocol so tools and models connect the same way.

- An **MCP server** exposes tools, data, or prompts.
- An **MCP client** in your app connects to any server.
- Write a tool once and use it from any MCP-aware agent.

Think of MCP as a common plug between models and the systems they use.
