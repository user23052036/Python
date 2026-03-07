Entity: collections.deque

`deque` (double-ended queue) supports efficient insertion and removal from **both ends**. Below are the **core operations you should know**, especially for algorithms and competitive programming.

---

# 1. Insert Operations

### `append(x)`

Insert element at the **right end**.

```python
from collections import deque

dq = deque()
dq.append(10)
dq.append(20)
print(dq)
```

Result

```
deque([10, 20])
```

Time complexity: **O(1)**

---

### `appendleft(x)`

Insert element at the **left end**.

```python
dq.appendleft(5)
```

Result

```
deque([5, 10, 20])
```

Time complexity: **O(1)**

---

# 2. Remove Operations

### `pop()`

Remove element from the **right end**.

```python
dq.pop()
```

Removes:

```
20
```

Time complexity: **O(1)**

---

### `popleft()`

Remove element from the **left end**.

```python
dq.popleft()
```

Removes:

```
5
```

Time complexity: **O(1)**

This operation is why `deque` is used for **BFS queues**.

---

# 3. Utility Operations

### `extend(iterable)`

Add multiple elements to the **right side**.

```python
dq.extend([30, 40])
```

Result

```
deque([10, 30, 40])
```

---

### `extendleft(iterable)`

Add multiple elements to the **left side**.

```python
dq.extendleft([1,2,3])
```

Result

```
deque([3,2,1,10,30,40])
```

Note: order is **reversed**.

---

### `clear()`

Remove all elements.

```python
dq.clear()
```

---

### `count(x)`

Count occurrences.

```python
dq.count(10)
```

---

### `remove(value)`

Remove the **first occurrence**.

```python
dq.remove(10)
```

---

# 4. Rotation Operations

### `rotate(k)`

Rotate elements.

```python
dq = deque([1,2,3,4])
dq.rotate(1)
```

Result

```
deque([4,1,2,3])
```

Left rotation:

```python
dq.rotate(-1)
```

Result

```
deque([1,2,3,4])
```

---

# 5. Access Operations

You can index like a list:

```python
dq[0]
dq[-1]
```

But random access is **O(n)**.

---
