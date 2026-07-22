That's because **most of the time you weren't appending the same mutable object repeatedly.** This is a subtle but extremely important distinction.

There are **three common cases**.

### Case 1: Appending a brand new list each time (No `.copy()` needed)

```python
res = []

for i in range(3):
    temp = [i]
    res.append(temp)

print(res)
```

Output:

```python
[[0], [1], [2]]
```

Here, `temp = [i]` creates a **new list** on every iteration.

Memory-wise:

```
res
 |
 +--> [0]
 |
 +--> [1]
 |
 +--> [2]
```

Every append stores a different object.

---

### Case 2: Reusing the same list (Need `.copy()`)

```python
res = []
temp = []

for i in range(3):
    temp.append(i)
    res.append(temp)

print(res)
```

Output:

```python
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

Why?

There is only **one** `temp`.

```
res
 |
 +------+
 |      |
 |      |
 |      |
 +------+
        |
     [0,1,2]
```

Every element of `res` points to the same list.

---

### Case 3: Backtracking (Always reuse the same list)

This is exactly what happens in your subsets solution.

```python
subset = []

def dfs(i):
    ...
    subset.append(nums[i])
    dfs(i + 1)
    subset.pop()
```

Notice something?

You never write

```python
subset = []
```

inside `dfs`.

There is only **one** `subset` for the entire recursion.

You're repeatedly changing

```
[]
↓
[1]
↓
[1,2]
↓
[1]
↓
[]
↓
[2]
↓
[]
```

Since it's the **same object**, you must save a snapshot:

```python
res.append(subset.copy())
```

---

## You can prove this yourself

Run this:

```python
subset = []

print(id(subset))

subset.append(1)
print(id(subset))

subset.pop()
print(id(subset))
```

Output:

```
140657832...
140657832...
140657832...
```

The `id` never changes.

Now try:

```python
temp = [1]
print(id(temp))

temp = [1, 2]
print(id(temp))
```

Output:

```
140657832...
140657945...
```

The `id` changes because you created a new list.

---

### A rule you'll use throughout DSA

If you see code like:

```python
path = []

def dfs(...):
    path.append(...)
    dfs(...)
    path.pop()
```

then **when saving the answer**, use:

```python
ans.append(path.copy())
```

because `path` is reused.

If, instead, you're creating a fresh list each time, such as:

```python
new_path = path + [nums[i]]
dfs(new_path)
```

then `.copy()` is unnecessary because `path + [nums[i]]` already creates a new list.

This distinction—**reusing one mutable object vs. creating a new object**—is one of the most important concepts in Python backtracking. Once it clicks, many recursive algorithms become much easier to understand.
