`append()` adds **one item** to a list, even if that item is another list.

```python
A = [1]
A.append([2, 3, 4, 5])
# A becomes: [1, [2, 3, 4, 5]]
# length = 2
```

To add elements **individually**, use `extend()`:

```python
A = [1]
A.extend([2, 3, 4, 5])
# A becomes: [1, 2, 3, 4, 5]
# length = 5
```

You cannot write:

```python
A.extend(1,2,3,4,5)
```

because `extend()` takes **only one iterable argument**.

Correct examples:

```python
A.extend([1,2,3,4,5])
A.extend((1,2,3,4,5))
A.extend(range(1,6))
```

Also, this works like `extend()`:

```python
A += [2, 3, 4, 5]
```

---

Here is the breakdown of how these two sorting methods work in Python.
## The Big Difference: L.sort() vs sorted(L)

* L.sort() modifies in-place: This method changes the original list directly and returns None. Use this to save memory.
* sorted(L) creates a copy: This function leaves the original list untouched and returns a brand-new sorted list. Use this to keep your original data. [1, 2, 3, 4] 

## Code Examples

# Example 1: Using L.sort()L = [1, 3, 2]
L.sort()
print(L)  # Output: [1, 2, 3] (The original list changed)
# Example 2: Overwriting with sorted()L = [1, 3, 2]L = sorted(L)
print(L)  # Output: [1, 2, 3] (The original list was replaced)

To help you practice further, I can show you how to use the reverse=True argument for descending order, or how to sort more complex data like lists of dictionaries. Which one would you like to see? [5] 

---

