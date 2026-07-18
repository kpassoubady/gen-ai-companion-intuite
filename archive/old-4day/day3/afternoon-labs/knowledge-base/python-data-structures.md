# Python Data Structures

## Lists

Lists are ordered, mutable sequences. They can contain mixed types but typically hold homogeneous data.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert(1, "avocado")
print(fruits[0])        # "apple"
print(fruits[-1])       # "date"
print(fruits[1:3])      # ["avocado", "banana"]
```

Lists support common operations: append, insert, remove, pop, sort, reverse, and slicing. List comprehensions provide a concise way to create lists.

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

Time complexity: O(1) for append and index access, O(n) for insert and search.

## Tuples

Tuples are ordered, immutable sequences. Use them for fixed collections of data.

```python
point = (3, 4)
x, y = point         # tuple unpacking
rgb = (255, 128, 0)
```

Tuples are hashable (if all elements are hashable), so they can be dictionary keys or set members. They use less memory than lists.

## Dictionaries

Dictionaries store key-value pairs with O(1) average lookup time. Keys must be hashable (strings, numbers, tuples).

```python
user = {"name": "Alice", "age": 30, "role": "developer"}
print(user["name"])           # "Alice"
user["email"] = "alice@dev.io"
print(user.get("phone", "N/A"))  # "N/A" (default)
```

Common dictionary operations:

- `dict.keys()` — all keys
- `dict.values()` — all values
- `dict.items()` — key-value pairs
- `dict.update()` — merge another dict
- `dict.pop(key)` — remove and return value

Dictionary comprehensions:

```python
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

Since Python 3.7, dictionaries maintain insertion order.

## Sets

Sets are unordered collections of unique elements. They support mathematical set operations.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)    # union: {1, 2, 3, 4, 5, 6}
print(a & b)    # intersection: {3, 4}
print(a - b)    # difference: {1, 2}
```

Sets are useful for removing duplicates and membership testing (O(1) average).

## Collections Module

The `collections` module provides specialized data structures:

- `defaultdict` — dict with default factory for missing keys
- `Counter` — dict subclass for counting hashable objects
- `OrderedDict` — dict that remembers insertion order (less needed since Python 3.7)
- `deque` — double-ended queue with O(1) append/pop on both ends
- `namedtuple` — tuple subclass with named fields

```python
from collections import Counter, defaultdict, deque

word_counts = Counter("hello world".split())
graph = defaultdict(list)
queue = deque([1, 2, 3])
queue.appendleft(0)
```
