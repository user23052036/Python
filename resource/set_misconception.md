### 1. The correct rule

The `set()` constructor expects an **iterable**.

### 2. Tuples **are iterable**

Your assumption:

> tuples are indexable so they are not iterable

This is wrong.

Tuples are **both**:

* iterable
* indexable

Example:

```python
t = (10,20,30)

for x in t:
    print(x)
```

Output

```
10
20
30
```

That loop works **only because tuples are iterable**.

---

### 3. What happens in `set(start)`

If

```python
start = (0,0)
```

then

```python
set(start)
```

means:

```
iterate through the tuple
add each element to the set
```

So Python sees

```
0
0
```

Sets remove duplicates → result:

```python
{0}
```

---

### 4. What happens in `set([start])`

Here the iterable is:

```
[(0,0)]
```

Python iterates the list:

```
(0,0)
```

So the set becomes:

```
{(0,0)}
```

---

### 5. Cleanest solution

Just write:

```python
visited = {start}
```

This directly creates a set containing the tuple.

---

### Quick mental model

| Code           | Iterable  | Result    |
| -------------- | --------- | --------- |
| `set(start)`   | `(0,0)`   | `{0}`     |
| `set([start])` | `[(0,0)]` | `{(0,0)}` |
| `{start}`      | literal   | `{(0,0)}` |

---

### One deeper thing (important for algorithms)

Your coordinates `(r,c)` work inside sets because tuples are **hashable**.

Lists are **not**.

So this would crash:

```python
visited = {[0,0]}
```

Error:

```
TypeError: unhashable type: 'list'
```

That’s why **graph/grid algorithms almost always store nodes as tuples**.

---
