`assert` is a debugging tool. It checks whether a condition is **True**. If it is, the program continues. If it is **False**, Python immediately raises an `AssertionError`.

Syntax:

```python
assert condition
```

or

```python
assert condition, "Error message"
```

---

## Example 1: Checking array size

Suppose the input format says:

```
5
1 2 3 4 5
```

You expect exactly 5 numbers.

```python
n = int(input())
arr = list(map(int, input().split()))

assert len(arr) == n

print(arr)
```

### Input

```
5
1 2 3 4 5
```

Output

```
[1, 2, 3, 4, 5]
```

The assertion passes because:

```
len(arr) = 5
n = 5
```

---

### If the input is wrong

Input

```
5
1 2 3
```

Now

```python
len(arr)
```

is

```
3
```

but

```
n = 5
```

So

```python
assert len(arr) == n
```

becomes

```python
assert 3 == 5
```

which is False.

Python stops with

```python
AssertionError
```

---

## Example 2: With an error message

```python
assert len(arr) == n, "Array size does not match n"
```

Now the output is

```
AssertionError: Array size does not match n
```

This is much easier to understand than a plain `AssertionError`.

---

# Example 3: Validating assumptions

Suppose your algorithm requires a sorted array.

```python
arr = [1, 2, 3, 4]

assert arr == sorted(arr)

# Binary Search
```

If someone accidentally passes

```python
arr = [4, 2, 1]
```

your program immediately stops instead of producing an incorrect result.

---

# Example 4: Positive numbers only

```python
x = int(input())

assert x > 0, "x must be positive"

print(x)
```

Input

```
5
```

Works.

Input

```
-3
```

Output

```
AssertionError: x must be positive
```

---

# Should you use `assert` in placement OAs?

**Usually, no.**

In coding interviews and online assessments:

* The platform guarantees that the input follows the problem statement.
* If the statement says `n = 5`, there will be 5 numbers.
* Adding assertions is unnecessary and can even cause your solution to fail if the platform disables or handles them differently.

Most competitive programmers simply write:

```python
n = int(input())
arr = list(map(int, input().split()))
```

and trust the input.

---

# When is `assert` actually useful?

Use it while:

* Debugging your own code.
* Verifying assumptions during development.
* Checking that helper functions receive valid data.
* Catching bugs early in larger projects.

For example, if you write your own function:

```python
def binary_search(arr, target):
    assert arr == sorted(arr), "Array must be sorted"

    # Binary Search implementation
```

If you accidentally call it with an unsorted array, you'll immediately know the problem.

---

## Rule of thumb

* **LeetCode / Codeforces / Placement OA:** Rarely use `assert`.
* **Personal projects / Debugging / Learning:** `assert` is very useful for catching mistakes early.
