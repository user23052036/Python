`collections.deque` (**double-ended queue**) is one of the most useful data structures in Python. It is implemented as a doubly linked structure optimized for inserting and removing elements from both ends.

```python
from collections import deque

dq = deque()
```

---

# 1. Stack Operations (LIFO)

### Push

```python
dq.append(10)
dq.append(20)
dq.append(30)

print(dq)
# deque([10, 20, 30])
```

### Pop

```python
x = dq.pop()

print(x)   # 30
print(dq)  # deque([10, 20])
```

### Peek Top

```python
print(dq[-1])  # 20
```

### Time Complexity

| Operation     | Complexity |
| ------------- | ---------- |
| append()      | O(1)       |
| pop()         | O(1)       |
| peek (dq[-1]) | O(1)       |

---

# 2. Queue Operations (FIFO)

### Enqueue

```python
dq.append(10)
dq.append(20)
dq.append(30)
```

### Dequeue

```python
x = dq.popleft()

print(x)  # 10
```

### Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| append()  | O(1)       |
| popleft() | O(1)       |

This is why `deque` is preferred over `list` for queues.

---

# 3. Insert at Front

```python
dq.appendleft(5)

print(dq)
# deque([5, 10, 20, 30])
```

### Complexity

```text
O(1)
```

---

# 4. Remove from Front

```python
dq.popleft()
```

### Complexity

```text
O(1)
```

---

# 5. Check Empty

```python
if dq:
    print("Not Empty")
else:
    print("Empty")
```

### Complexity

```text
O(1)
```

---

# 6. Size

```python
len(dq)
```

### Complexity

```text
O(1)
```

---

# 7. Rotate

Moves elements cyclically.

```python
dq = deque([1, 2, 3, 4])

dq.rotate(1)

print(dq)
# deque([4, 1, 2, 3])
```

Rotate left:

```python
dq.rotate(-1)

print(dq)
# deque([1, 2, 3, 4])
```

### Complexity

```text
O(k)
```

where `k` is the number of positions rotated.

---

# 8. Bounded Deque

Keeps only the most recent elements.

```python
dq = deque(maxlen=3)

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)

print(dq)
# deque([2, 3, 4], maxlen=3)
```

Very useful for sliding window problems.

---

# 9. Common Interview Patterns

### Monotonic Stack

```python
stack = deque()

while stack and stack[-1] < num:
    stack.pop()

stack.append(num)
```

---

### BFS

```python
from collections import deque

q = deque([start])

while q:
    node = q.popleft()

    for nei in graph[node]:
        q.append(nei)
```

---

### Sliding Window Maximum

```python
dq = deque()

for i in range(len(nums)):

    while dq and nums[dq[-1]] < nums[i]:
        dq.pop()

    dq.append(i)

    if dq[0] <= i-k:
        dq.popleft()
```

---

# Space Complexity

A deque storing `n` elements requires:

```text
O(n)
```

space.

---

# `list` vs `deque`

| Operation      | list           | deque |
| -------------- | -------------- | ----- |
| append()       | O(1) amortized | O(1)  |
| pop() from end | O(1)           | O(1)  |
| insert(0,x)    | O(n)           | O(1)  |
| pop(0)         | O(n)           | O(1)  |
| appendleft()   | Not available  | O(1)  |
| popleft()      | O(n)           | O(1)  |

For **stacks**, both `list` and `deque` are fine.

For **queues**, BFS, sliding windows, monotonic queues, or frequent front operations, use `deque`. That's why you'll see almost every BFS solution on LeetCode start with:

```python
from collections import deque

q = deque()
```
