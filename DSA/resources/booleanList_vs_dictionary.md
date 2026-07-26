This is a good optimization question. The answer is **no**. In fact, a dictionary will usually be **slower**.

Let's compare.

| Operation        | Boolean List | Dictionary                           |
| ---------------- | ------------ | ------------------------------------ |
| Access           | O(1)         | O(1) average                         |
| Update           | O(1)         | O(1) average                         |
| Memory           | O(n)         | More than O(n) (hash table overhead) |
| CPU Cache        | Excellent    | Poor                                 |
| Hash Computation | ❌ None       | ✔ Required                           |

---

## Why is a list faster?

Suppose

```python
used = [False, False, False, False]
```

Accessing

```python
used[2]
```

is simply:

> "Go to the 3rd memory location."

No hashing.
No lookup.

---

With a dictionary

```python
used = {
    0: False,
    1: False,
    2: False,
    3: False
}
```

Accessing

```python
used[2]
```

requires:

1. Compute hash of key `2`
2. Find the correct bucket
3. Compare keys
4. Return the value

Even though it's still average O(1), it has a much larger constant cost.

---

## Another issue

Your duplicate check is

```python
if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
```

With a list:

```python
used[i-1]
```

is very natural.

With a dictionary:

```python
used[i-1]
```

works too, but you're paying hashing overhead for something that's just an array index.

---

## When is a dictionary useful?

A dictionary becomes useful when your keys are **not consecutive indices**.

Example:

```python
visited = {
    "A": True,
    "B": False,
    "Delhi": True
}
```

or

```python
visited = {
    (3,5): True,
    (4,7): False
}
```

Here, a list doesn't make sense.

---

## Rule of thumb (worth remembering)

```python
# If the state is based on ARRAY INDICES:
#
#       used = [False] * n
#
# is almost always the fastest choice.
#
# If the state is based on arbitrary KEYS:
#
#       visited = {}
#
# or
#
#       visited = set()
#
# is the right choice.
```

---

### One more thought

You're asking the kind of questions that interviewers like:

> "Can I replace this data structure with another one to optimize it?"

Just remember that **asymptotic complexity isn't the whole story**. Both a list and a dictionary give O(1) access on average, but the list wins because its **constant factors are much smaller**. When your state is indexed by `0...n-1`, a boolean list is the most efficient representation.
