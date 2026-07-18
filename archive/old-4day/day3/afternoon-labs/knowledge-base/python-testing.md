# Python Testing

## Why Test?

Testing ensures code works as expected, prevents regressions, and documents intended behavior. Python has excellent testing tools built in and available via third-party packages.

## unittest

Python's built-in testing framework:

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            add("hello", 5)

if __name__ == "__main__":
    unittest.main()
```

Run with: `python -m unittest test_module.py`

## pytest

The most popular Python testing framework. Simpler syntax, better output, powerful fixtures.

```python
# test_calculator.py
def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_strings():
    assert add("hello ", "world") == "hello world"
```

Run with: `pytest test_calculator.py -v`

### Fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    return {"users": ["Alice", "Bob"], "count": 2}

def test_user_count(sample_data):
    assert sample_data["count"] == len(sample_data["users"])

def test_user_names(sample_data):
    assert "Alice" in sample_data["users"]
```

### Parametrize

```python
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## Mocking

Replace real objects with test doubles to isolate the code under test:

```python
from unittest.mock import patch, MagicMock

def fetch_user(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")
    return response.json()

def test_fetch_user():
    mock_client = MagicMock()
    mock_client.get.return_value.json.return_value = {"name": "Alice"}

    result = fetch_user(mock_client, 42)
    assert result["name"] == "Alice"
    mock_client.get.assert_called_once_with("/users/42")
```

### Patching

```python
@patch("module.requests.get")
def test_api_call(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"status": "ok"}

    result = my_api_function()
    assert result["status"] == "ok"
```

## Test Organization

```
project/
    src/
        calculator.py
        user_service.py
    tests/
        test_calculator.py
        test_user_service.py
        conftest.py          # shared fixtures
```

## Code Coverage

Measure how much of your code is executed by tests:

```bash
pip install pytest-cov
pytest --cov=src tests/ --cov-report=html
```

Aim for 80%+ coverage on critical paths. 100% coverage does not guarantee bug-free code.

## Best Practices

1. Test behavior, not implementation details
2. Keep tests independent (no shared state between tests)
3. Use descriptive test names that explain the expected behavior
4. Follow the Arrange-Act-Assert pattern
5. Test edge cases: empty inputs, None, boundary values
6. Run tests frequently during development
7. Use CI/CD to run tests on every commit
8. Mock external dependencies (APIs, databases, file system)
