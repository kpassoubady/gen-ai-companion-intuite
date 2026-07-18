"""
Lab 4.2 — Caching & Cost Measurement
Day 4 — Session 2

Goal: Add caching to a chatbot and measure token/cost savings.

Requirements:
1. Implement an in-memory response cache with TTL
2. Track cache hits vs misses
3. Count tokens for every API call (input + output)
4. Calculate and display cost savings from caching
5. Add a /stats command showing usage and savings

Stretch goals:
- Implement model tiering (simple queries use mini, complex use default)
- Add a budget guard that switches to mini when daily budget is 80% spent
- Track per-query cost breakdown

Run: python3 lab4_2_caching_cost.py
"""

import os
import sys

# Ensure the root of the repo is in the python path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import hashlib
import time
import tiktoken
from shared import get_completion, show_config


# ---------------------------------------------------------------------------
# Response cache
# ---------------------------------------------------------------------------
class ResponseCache:
    """In-memory cache with TTL for LLM responses."""

    def __init__(self, ttl_seconds=3600):
        # TODO: Initialize cache data structure
        # Hint:
        # self.cache = {}
        # self.ttl = ttl_seconds
        # self.hits = 0
        # self.misses = 0
        # self.saved_tokens = 0

        self.cache = {}
        self.ttl = ttl_seconds
        self.hits = 0
        self.misses = 0
        self.saved_tokens = 0

    def _make_key(self, query):
        """Create a cache key from a query."""
        return hashlib.md5(query.lower().strip().encode()).hexdigest()

    def get(self, query):
        """Retrieve a cached response if it exists and hasn't expired."""
        # TODO: Implement cache lookup
        # 1. Generate cache key
        # 2. Check if key exists and hasn't expired (compare timestamps)
        # 3. If hit: increment hits counter, track saved tokens, return response
        # 4. If miss: increment misses counter, return None

        # Hint:
        # key = self._make_key(query)
        # entry = self.cache.get(key)
        # if entry and time.time() - entry["timestamp"] < self.ttl:
        #     self.hits += 1
        #     self.saved_tokens += entry.get("tokens_saved", 0)
        #     return entry["response"]
        # self.misses += 1
        # return None

        return None  # TODO: replace

    def set(self, query, response, tokens_used=0):
        """Store a response in the cache."""
        # TODO: Implement cache storage
        # Hint:
        # key = self._make_key(query)
        # self.cache[key] = {
        #     "response": response,
        #     "timestamp": time.time(),
        #     "tokens_saved": tokens_used,
        # }

        pass  # TODO: replace

    def stats(self):
        """Return cache statistics."""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return {
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": f"{hit_rate:.1f}%",
            "entries": len(self.cache),
            "saved_tokens": self.saved_tokens,
        }


# ---------------------------------------------------------------------------
# Usage tracker
# ---------------------------------------------------------------------------
class UsageTracker:
    """Track API token usage and costs."""

    # Pricing per 1M tokens (update as needed)
    PRICING = {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    }

    def __init__(self):
        self.calls = []
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0.0

    def count_tokens(self, text, model="gpt-4o"):
        """Count tokens in a text string."""
        # TODO: Implement token counting
        # Hint:
        # enc = tiktoken.encoding_for_model(model)
        # return len(enc.encode(text))

        return 0  # TODO: replace

    def log_call(self, messages, response, model="gpt-4o-mini"):
        """Log an API call with token counts and cost."""
        # TODO: Implement call logging
        # 1. Count input tokens (sum of all message contents)
        # 2. Count output tokens (response text)
        # 3. Calculate cost based on model pricing
        # 4. Store in self.calls list
        # 5. Update totals

        # Hint:
        # input_tokens = sum(
        #     self.count_tokens(m["content"], model) for m in messages
        # ) + len(messages) * 4
        # output_tokens = self.count_tokens(response, model)
        #
        # pricing = self.PRICING.get(model, self.PRICING["gpt-4o-mini"])
        # cost = ((input_tokens / 1_000_000) * pricing["input"]
        #         + (output_tokens / 1_000_000) * pricing["output"])
        #
        # self.calls.append({
        #     "input_tokens": input_tokens,
        #     "output_tokens": output_tokens,
        #     "cost": cost,
        #     "model": model,
        #     "timestamp": time.time(),
        # })
        # self.total_input_tokens += input_tokens
        # self.total_output_tokens += output_tokens
        # self.total_cost += cost
        #
        # return input_tokens + output_tokens

        return 0  # TODO: replace

    def summary(self):
        """Return usage summary."""
        return {
            "total_calls": len(self.calls),
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_cost_usd": f"${self.total_cost:.6f}",
            "avg_tokens_per_call": (
                (self.total_input_tokens + self.total_output_tokens)
                // max(len(self.calls), 1)
            ),
        }


# ---------------------------------------------------------------------------
# Budget guard
# ---------------------------------------------------------------------------
class BudgetGuard:
    """Prevent spending beyond a daily budget."""

    def __init__(self, daily_limit_usd=1.0):
        self.daily_limit = daily_limit_usd
        self.daily_spend = 0.0
        self.blocked_count = 0

    def check_budget(self, estimated_cost=0.001):
        """Return True if the call is within budget."""
        # TODO (Stretch): Implement budget checking
        # Hint:
        # if self.daily_spend + estimated_cost > self.daily_limit:
        #     self.blocked_count += 1
        #     return False
        # return True

        return True  # TODO: replace

    def record_spend(self, actual_cost):
        """Record actual spending."""
        self.daily_spend += actual_cost


# ---------------------------------------------------------------------------
# Chatbot with caching and cost tracking
# ---------------------------------------------------------------------------
SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a helpful Python assistant. "
        "Keep responses concise and under 150 words."
    ),
}


def main():
    show_config()
    print("\n💰 Cached Chatbot — Lab 4.2")
    print("Commands: /stats, /clear, /cache, quit/exit")
    print("-" * 50)

    conversation = [SYSTEM_MESSAGE]
    cache = ResponseCache(ttl_seconds=600)  # 10 min TTL
    tracker = UsageTracker()
    budget = BudgetGuard(daily_limit_usd=1.0)

    while True:
        try:
            user_input = input("\n👤 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        if user_input == "/stats":
            print("\n📊 Usage Statistics:")
            for key, val in tracker.summary().items():
                print(f"   {key}: {val}")
            print("\n📦 Cache Statistics:")
            for key, val in cache.stats().items():
                print(f"   {key}: {val}")
            print(f"\n💳 Budget: ${budget.daily_spend:.6f} / "
                  f"${budget.daily_limit:.2f} "
                  f"({budget.blocked_count} blocked)")
            continue

        if user_input == "/cache":
            stats = cache.stats()
            print(f"\n📦 Cache: {stats['entries']} entries, "
                  f"{stats['hit_rate']} hit rate, "
                  f"{stats['saved_tokens']} tokens saved")
            continue

        if user_input == "/clear":
            conversation = [SYSTEM_MESSAGE]
            print("🔄 Conversation cleared.")
            continue

        # Check cache first
        cached = cache.get(user_input)
        if cached:
            print(f"\n🤖 Bot (cached): {cached}")
            continue

        # Check budget
        if not budget.check_budget():
            print("\n⚠️  Daily budget exceeded. Using cached responses only.")
            continue

        # Make API call
        conversation.append({"role": "user", "content": user_input})

        try:
            response = get_completion(conversation, tier="mini")
            print(f"\n🤖 Bot: {response}")

            # Track usage
            tokens = tracker.log_call(conversation, response, model="gpt-4o-mini")

            # Cache the response
            cache.set(user_input, response, tokens_used=tokens)

            # Record spending
            if tracker.calls:
                budget.record_spend(tracker.calls[-1].get("cost", 0))

            conversation.append({"role": "assistant", "content": response})

        except Exception as e:
            print(f"\n❌ Error: {e}")
            conversation.pop()  # remove failed user message

    # Final stats
    print("\n" + "=" * 50)
    print("📊 Final Statistics:")
    for key, val in tracker.summary().items():
        print(f"   {key}: {val}")
    print("\n📦 Cache Performance:")
    for key, val in cache.stats().items():
        print(f"   {key}: {val}")
    print("=" * 50)
    print("✅ Lab 4.2 complete!")


if __name__ == "__main__":
    main()
