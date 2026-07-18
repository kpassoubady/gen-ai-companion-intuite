# Python Functions

## Defining Functions

Functions are defined with the `def` keyword. They can accept parameters and return values.

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # "Hello, Alice!"
```

## Parameters and Arguments

### Default Parameters

```python
def connect(host, port=5432, timeout=30):
    print(f"Connecting to {host}:{port} (timeout={timeout}s)")

connect("localhost")                   # uses defaults
connect("localhost", port=3306)        # override port
connect("db.example.com", 5432, 60)   # positional args
```

### *args and **kwargs

```python
def log(*args, **kwargs):
    """Accept any number of positional and keyword arguments."""
    print("Args:", args)
    print("Kwargs:", kwargs)

log("error", "connection failed", level="CRITICAL", code=500)
# Args: ("error", "connection failed")
# Kwargs: {"level": "CRITICAL", "code": 500}
```

### Type Hints

```python
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    return length * width
```

Type hints are not enforced at runtime but help with documentation, IDE support, and static analysis tools like mypy.

## Return Values

Functions can return multiple values using tuples:

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)  # q=3, r=2
```

Functions without a return statement return `None`.

## Lambda Functions

Short anonymous functions for simple operations:

```python
square = lambda x: x ** 2
add = lambda a, b: a + b

# Common use: sorting with a key
users = [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]
sorted_users = sorted(users, key=lambda u: u["age"])
```

## Decorators

Decorators modify function behavior without changing their code:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"
```

Common built-in decorators: `@staticmethod`, `@classmethod`, `@property`.

## Generators

Functions that yield values one at a time, saving memory for large datasets:

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num, end=" ")
# 0 1 1 2 3 5 8 13 21 34
```

Generator expressions:

```python
squares = (x**2 for x in range(1000000))  # lazy evaluation
```

## Closures

A closure is a function that remembers variables from its enclosing scope:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15
```

## Best Practices

1. Keep functions small and focused (single responsibility)
2. Use descriptive names that start with a verb
3. Add docstrings for public functions
4. Use type hints for parameters and return values
5. Prefer returning values over modifying globals
6. Limit parameters to 3-4; use a config object for more
7. Make functions pure (no side effects) when possible
