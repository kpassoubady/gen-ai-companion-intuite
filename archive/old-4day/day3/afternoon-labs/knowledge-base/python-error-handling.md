# Python Error Handling

## Exception Basics

Python uses exceptions to handle errors at runtime. When an error occurs, Python raises an exception that can be caught and handled.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Common Exception Types

- `ValueError` — wrong value for the expected type (e.g., `int("abc")`)
- `TypeError` — wrong type for an operation (e.g., `"hello" + 5`)
- `KeyError` — dictionary key not found
- `IndexError` — list index out of range
- `FileNotFoundError` — file does not exist
- `AttributeError` — object has no such attribute
- `ImportError` — module not found
- `ZeroDivisionError` — division or modulo by zero
- `NameError` — variable not defined
- `SyntaxError` — invalid Python syntax (caught at parse time)

## Try/Except/Else/Finally

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
else:
    # Runs only if no exception was raised
    print(f"Read {len(content)} characters")
finally:
    # Runs always, even if an exception was raised
    file.close()
```

The `else` block runs only when no exception occurs. The `finally` block runs regardless, making it ideal for cleanup.

## Raising Exceptions

```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Expected int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age must be 0-150, got {age}")
    return age
```

## Custom Exceptions

Create custom exceptions by inheriting from `Exception`:

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount}. Balance: ${balance}"
        )

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount
```

## Context Managers

The `with` statement ensures resources are properly cleaned up:

```python
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed, even if an exception occurs
```

Create custom context managers with `__enter__` and `__exit__` methods or the `contextlib` module.

## Best Practices

1. Catch specific exceptions, not bare `except:`
2. Keep try blocks small and focused
3. Use `else` for code that should run only on success
4. Use `finally` or context managers for cleanup
5. Raise exceptions early, catch them late
6. Include helpful error messages
7. Log exceptions before handling them in production
8. Never silently swallow exceptions (`except: pass`)
