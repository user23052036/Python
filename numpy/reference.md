## **1. arange() method**

`np.arange()` creates a sequence of numbers with a specified **start**, **stop**, and **step**—similar to Python’s `range()`, but it returns a **NumPy array** instead of a Python list.

Here’s the idea:

### **Basic usage**

```python
import numpy as np

a = np.arange(5)
print(a)   # [0 1 2 3 4]
```

### **With start and stop**

```python
np.arange(2, 10)
# [2 3 4 5 6 7 8 9]
```

### **With step**

```python
np.arange(0, 10, 2)
# [0 2 4 6 8]
```

### **With float step**

```python
np.arange(0, 1, 0.2)
# [0.  0.2 0.4 0.6 0.8]
```

### **But important note**

`np.arange()` can have **precision issues with floats** (because binary floating-point).
If you need accurate evenly spaced numbers, use:

```python
np.linspace(start, stop, num_points)
```


<br>
<br>

## **2. `np.arange()` vs `np.linspace()`**

`arange(start, stop, step)` keeps **adding step** repeatedly until the next value would be ≥ stop.

### Example

```python
np.arange(0, 1, 0.1)
```

Expected?
`[0.0, 0.1, 0.2, ... 0.9]`

Actual?
Sometimes you get:

```
[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
```

…but for some floating values you may see:

```
[0.   0.3  0.6  0.89999999]
```

Because 0.3, 0.6, … cannot be represented exactly in binary.

### **How `np.linspace()` behaves**

`linspace(start, stop, num_points)` creates **exactly N points**, including the **stop** value.

### Example

```python
np.linspace(0, 1, 5)
```

Output:

```
[0.   0.25 0.5  0.75 1.0]
```

Perfect spacing.
No floating-point accumulation.

---

## **When to use what**

### ✔ Use **`np.arange()`** when:

* You want array sizes **dependent on step**
* You don't care about tiny FP errors
* You want speed and simple integer sequences

Good for:

```python
idx = np.arange(1000)     # indexing
t = np.arange(0, 10, 0.1) # time steps (approx)
```

---

### ✔ Use **`np.linspace()`** when:

* You need **precision**
* You need **exact number of points**
* You need the **endpoint included**

Good for:

```python
x = np.linspace(0, 2*np.pi, 1000)
```

---

## **Quick visual difference**

| Method                      | How it works                                       | Best for                      |
| --------------------------- | -------------------------------------------------- | ----------------------------- |
| `arange(start, stop, step)` | Keeps adding step → may accumulate floating errors | Iterations, approximate steps |
| `linspace(start, stop, n)`  | Divides interval into equal parts                  | Math, graphs, ML data         |

<br>
<br>

## **3. `ravel()` vs `flatten()`**

Here’s the crisp, no-nonsense difference:

**`ravel()`**

* Returns a **view** of the array whenever possible.
* **No copy** → faster and memory-efficient.
* If the original array changes, the raveled array may also change.

**`flatten()`**

* **Always returns a copy**.
* Safe, independent array.
* Changes in the original array won’t affect the result.

**In short:** `ravel()` = view (no copy, faster). `flatten()` = copy (safer).

<br>
<br>

## **4. Mask in numpy**

### ✔ What is a mask in NumPy?

A **mask** is simply a NumPy array of Boolean values (`True/False`) that has the **same shape** as the original array.

Example:

```python
numbers = np.array([1,2,3,4,5,6,7])
mask = numbers > 5
```

The mask becomes:

```
[False False False False False  True  True]
```

So yes — it **is** stored as an array.

---

## 🔍 Why is its type `<class 'numpy.ndarray'>` ?

Because NumPy converts the expression:

```python
numbers > 5
```

into an array of True/False values.

So `mask` is literally:

```python
np.array([False, False, False, False, False, True, True])
```

Just like numbers was:

```python
np.array([1,2,3,4,5,6,7])
```

---

## ✔ How is the mask used?

You pass it back to the array:

```python
numbers[mask]
```

NumPy picks only the elements where mask is True.

So masking is like **filtering using a Boolean array**.

---

## 🔥 Simple visual:

```
numbers: [1 2 3 4 5 6 7]
mask:    [F F F F F T T]
--------------------------------
numbers[mask] --> [6 7]
```

---

## ⭐ Key takeaway

✔ Mask **is a NumPy array**
✔ It stores Boolean values
✔ It is used for filtering efficiently

<br>
<br>

## **5. where() vs masking**

You're absolutely right — they **feel** similar because both filter data — but they serve *different roles*.

Let’s clear it up in the simplest way 👇

---

### ✅ Both masking and `np.where()` find matching elements

But…

### ✔ Mask gives you **True/False array**

### ✔ `np.where()` gives you **index positions**

---

---

### 🔹 Visual Example

```python
arr = np.array([10, 20, 30, 40, 50])
```

### 🔸 Masking

```python
mask = arr > 25
print(mask)
```

Output:

```
[False False True True True]
```

✔ Mask answers: “Which positions match?”

If you apply it:

```python
arr[mask]
```

→ `[30 40 50]`

---

---

### 🔸 `np.where()`

```python
idx = np.where(arr > 25)
print(idx)
```

Output:

```
(array([2, 3, 4]),)
```

✔ `np.where()` answers: “Tell me the **index positions** that match.”

Then applying:

```python
arr[idx]
```

→ `[30 40 50]`

---

---

### 🔥 Simple Analogy

| You want YES/NO for each element → **Mask**
| You want exact positions → **np.where()** |

They work together:

```
mask   ==> boolean selection
where  ==> index lookup
```
---

### ✔ Mask summary

* **Type:** `numpy.ndarray`
* Stores **True/False** values for each element
* Directly filters elements → `[2 4 6 8 10]`

---

### ✔ `np.where()` summary

* **Type:** `tuple`
* Stores **index positions** where condition is True → `(array([7, 8, 9]),)`
* Those indices are then used to get values → `[8 9 10]`


## **6. `numpy.where(condition,x,y)` **


### ✅ What your code is actually doing

```python
where_indx = numpy.where(numbers > 7, numbers*3, numbers)
```

This is **not** the index-returning version of `where()`.

This version performs **conditional replacement**:

✔ if value > 7 → use value * 3
✔ else → keep original value

So `where_indx` becomes a **new array**, not indices.

Example result:

```
[1 2 3 4 5 6 7 24 27 30]
```

Type → `<class 'numpy.ndarray'>`

---

### ❌ Why this fails:

```python
numbers[where_indx]
```

Here you are trying to use that array as an **index array**,
but it contains values, not positions (and values > 9 → invalid index).

That’s why it's wrong.

---

---

### ✔ If you want indices (filtering)

Use:

```python
idx = numpy.where(numbers > 7)
print(numbers[idx])
```

---

### ✔ If you want replacement (ternary style)

Use:

```python
result = numpy.where(numbers > 7, numbers*3, numbers)
print(result)
```

---

### 🔥 Final summary:

| Expression                  | What it returns                    |
| --------------------------- | ---------------------------------- |
| `np.where(condition)`       | indices (tuple)                    |
| `np.where(condition, x, y)` | transformed array, **not indices** |


## **7. `vstack()` vs `hstack()` **


### **`np.vstack()` (Vertical Stack)**

Think of stacking arrays **on top of each other** like layers.

* It joins arrays **row-wise** (adds new rows).
* Result height increases.

### Example:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.vstack((a, b))
print(result)
```

**Output:**

```
[[1 2 3]
 [4 5 6]]
```

---

### **`np.hstack()` (Horizontal Stack)**

Think of placing arrays **side-by-side**.

* It joins arrays **column-wise** (adds new columns).
* Same number of rows required.

### Example:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.hstack((a, b))
print(result)
```

**Output:**

```
[1 2 3 4 5 6]
```

<br>
<br>

## **8. `numpy.delete()`**

`np.delete()` works, but it needs **two things**:

1. the array
2. what to delete (index / slice / axis)

---

### ✔ Basic format

```python
np.delete(array, index, axis=None)
```

* `index` → where to delete
* `axis` → 0 for row, 1 for column
  (if omitted, it deletes from flattened array)

---

### ✅ Delete a **row**

Example: remove 2nd row (index 1)

```python
import numpy as np

original = np.array([[1,2,3],[4,5,6],[7,8,9]])

deleted_row = np.delete(original, 1, axis=0)
print(deleted_row)
```

✔ Output:

```
[[1 2 3]
 [7 8 9]]
```

---

### ✅ Delete a **column**

Example: remove 1st column (index 0)

```python
deleted_col = np.delete(original, 0, axis=1)
print(deleted_col)
```

✔ Output:

```
[[2 3]
 [5 6]
 [8 9]]
```

---

### ❗ If you use it without axis, numpy flattens array first

```python
np.delete(original, 3)
```

This deletes the 4th element from flattened list:

```
Flattened: [1 2 3 4 5 6 7 8 9]
After delete: [1 2 3 5 6 7 8 9]
```

---

### 📌 Delete multiple rows or columns

```python
np.delete(original, [0,2], axis=0)  # delete row 0 and 2
np.delete(original, [1], axis=1)    # delete 2nd column
```

The second parameter can't be empty — you must specify indices.

<br>
<br>
