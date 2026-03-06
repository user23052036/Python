
## ✅ Question 2

### Code:

```python
x = "abcdef"
i = "a"

while i in x:
    print("i", end=" ")
```

### Correct Answer:

**`i i i i i ...` (infinite)**

### Explanation:

* `i = "a"`
* `"a" in "abcdef"` → True
* Inside loop: `print("i")` → prints literal string `"i"`
* `i` never changes
* Condition always True

⚠ Infinite loop.

---

## ✅ Question 3

### Code:

```python
b = 0
for a in range(0, 10, 2):
    b += a + 1
```

### Step 1: Expand range

```
range(0, 10, 2)
→ 0, 2, 4, 6, 8
```

### Step 2: Calculate

| a | a+1 | b  |
| - | --- | -- |
| 0 | 1   | 1  |
| 2 | 3   | 4  |
| 4 | 5   | 9  |
| 6 | 7   | 16 |
| 8 | 9   | 25 |

### Correct Answer:

**25**

---

## ✅ Question 5

### Code:

```python
if(True):
    print("A")

if(100):
    print("B")

if(" "):
    print("C")

if([[]]):
    print("D")
```

---

## Evaluate each condition:

### 1️⃣ `if(True)`

True → prints A

### 2️⃣ `if(100)`

Non-zero number → True → prints B

### 3️⃣ `if(" ")`

Non-empty string → True → prints C

### 4️⃣ `if([[]])`

Outer list has 1 element → non-empty → True → prints D

---

### Final Output:

```
A
B
C
D
```

---

## Correct Boolean Concept Statement:

✔ True values:

* `True`
* Non-zero numbers
* Non-empty strings
* Non-empty containers (even if they contain empty containers)

✔ False values:

* `False`
* `None`
* `0`
* `""`
* `[]`
* `{}`

---

# ⚠ Key Concepts These Questions Test

1. Infinite loop logic
2. `range(start, stop, step)`
3. Python truthiness rules
4. Literal vs variable printing
5. Container truth evaluation

---

