
# 1  Basic definitions & vocabulary

## 1. Mutable vs Immutable

This property answers **one question only**:

> **Can the object change after it is created?**

#### Mutable (can change)

You can modify the object **without creating a new object**.

Examples: `list`, `dict`, `set`

#### Example

```python
a = [1,2,3]
a.append(4)
print(a)
```

Output

```
[1, 2, 3, 4]
```

The same list `a` was modified.

Another example with dictionary:

```python
d = {"a":1, "b":2}
d["c"] = 3
print(d)
```

Output

```
{'a':1,'b':2,'c':3}
```

The dictionary changed.

---

### Immutable (cannot change)

If you try to modify it, **Python creates a new object** or throws an error.

Examples: `tuple`, `str`, `int`, `frozenset`

### Example

```python
t = (1,2,3)
t[0] = 10
```

Error

```
TypeError: 'tuple' object does not support item assignment
```

Because tuples cannot change.

Another example with string:

```python
s = "hello"
s = s + " world"
```

A **new string** is created.

---

## 2. Hashable

This property answers a different question:

> **Can this object be used as a key in a dictionary or element in a set?**

Python uses a **hash function** internally for fast lookup.

Only objects whose value **never changes** can have a stable hash.

Therefore **hashable objects must be immutable**.

---

## Hashable examples

```python
a = {1,2,3}          # integers are hashable
b = {"apple","cat"}  # strings are hashable
c = {(1,2),(3,4)}    # tuples are hashable if elements are hashable
```

All valid.

---

## Not hashable

```python
s = {[1,2],[3,4]}
```

Error

```
TypeError: unhashable type: 'list'
```

Because lists can change.

---

## 3. Ordered

This property answers:

> **Does the collection maintain the order of elements?**

---

## Ordered structures

Elements appear **in the same order you inserted them**.

Examples:

* `list`
* `tuple`
* `dict` (Python 3.7+)

### Example

```python
a = [5,1,7]
print(a)
```

Output

```
[5,1,7]
```

The order is preserved.

Dictionary example:

```python
d = {"a":1,"b":2,"c":3}
print(d)
```

Output

```
{'a':1,'b':2,'c':3}
```

Insertion order maintained.

---

## Unordered structure

`set`

```python
s = {5,1,7}
print(s)
```

Output could be

```
{1,5,7}
```

or

```
{7,1,5}
```

The order is **not guaranteed**.

---

## 4. Indexable

This answers:

> **Can you access elements using numeric position?**

Example:

```python
a = [10,20,30]
print(a[0])
```

Output

```
10
```

So lists are indexable.

---

## Indexable structures

* list
* tuple
* string

Example

```python
t = (5,6,7)
print(t[1])
```

Output

```
6
```

---

## Not indexable

Dictionaries and sets.

Dictionary example:

```python
d = {"a":1,"b":2}
print(d[0])
```

Error

```
KeyError
```

Because dictionaries use **keys**, not positions.

Correct way:

```python
print(d["a"])
```

Output

```
1
```

### Example

```python
s = {10, 20, 30}

print(s[0])
```

Output:

```
TypeError: 'set' object is not subscriptable
```

Why?
A set does **not store elements by position**, so there is **no index 0, 1, 2...**

---

### How to access elements in a set

Use a **loop**:

```python
s = {10, 20, 30}

for x in s:
    print(x)
```

Output (order may vary):

```
10
20
30
```

---

### If you really need indexing

Convert the set to a list:

```python
s = {10,20,30}
l = list(s)

print(l[0])
```

But remember: **order is not guaranteed**, because sets are unordered.

---

## 5. Why these concepts overlap

Because a structure can satisfy **multiple properties simultaneously**.

Example: **List**

| Property  | Value |
| --------- | ----- |
| Mutable   | Yes   |
| Ordered   | Yes   |
| Indexable | Yes   |
| Hashable  | No    |

Example: **Tuple**

| Property  | Value |
| --------- | ----- |
| Mutable   | No    |
| Ordered   | Yes   |
| Indexable | Yes   |
| Hashable  | Yes   |

Example: **Set**

| Property  | Value |
| --------- | ----- |
| Mutable   | Yes   |
| Ordered   | No    |
| Indexable | No    |
| Hashable  | No    |

Example: **Dictionary**

| Property  | Value             |
| --------- | ----------------- |
| Mutable   | Yes               |
| Ordered   | Yes (Python 3.7+) |
| Indexable | No                |
| Hashable  | No                |

---

# 6. The most important exam summary

| Structure | Mutable | Ordered | Indexable | Hashable |
| --------- | ------- | ------- | --------- | -------- |
| List      | Yes     | Yes     | Yes       | No       |
| Tuple     | No      | Yes     | Yes       | Yes      |
| Set       | Yes     | No      | No        | No       |
| Dict      | Yes     | Yes     | No        | No       |

---

## 2 — Lists (`list`)

### Properties

* Mutable, ordered, indexable, can contain duplicates and mixed types.
* Dynamic size; append/pop/insert operations available.

### Common operations

```python
a = [1,2,3]
a.append(4)        # [1,2,3,4]
a.pop()            # removes and returns last item (4)
a.pop(1)           # removes index 1
a.insert(1, 9)     # [1,9,2,3]
a[0] = 10          # mutate element
len(a)
a.index(2)         # index of first occurrence
```

### Iteration & search

* Linear time `O(n)` for `index`, membership `in` is `O(n)`.

### Example: find index of max

```python
myList = [1,5,5,5,1]
max_val = myList[0]
indexOfMax = 0
for i in range(1, len(myList)):
    if myList[i] > max_val:
        max_val = myList[i]
        indexOfMax = i
print(indexOfMax)   # prints 1 (first occurrence of the maximum)
```

Complexity `O(n)`. Note: equality check (`==`) does not update index — returns first max index.

### Pitfalls

* Mutating a list while iterating over it (e.g., removing items inside `for x in a:`) can skip items or behave unexpectedly.
* Avoid using lists as default args in functions (`def f(a=[]): ...`) because the same list object is reused.

---

## 3 — Tuples (`tuple`)

### Properties

* Immutable, ordered, indexable, can contain mixed types.
* Useful when data must not change: keys in dictionaries (if tuple elements are hashable), returning multiple values from functions.

### Create and convert

```python
t = (1,2,3)
t2 = tuple([1,2,3])
```

### Sorting tuples (example from quiz)

If you want to produce a new tuple sorted by string length:

```python
t = ('apple', 'orange', 'pear')
order = 'desc'  # or 'asc'
if 'asc' in order:
    st = sorted(t, key=len)
else:
    st = sorted(t, key=len, reverse=True)
print(tuple(st))
```

Notes:

* `sorted()` returns a list; convert back to `tuple()` if required.
* `key=len` sorts by length; `reverse=True` for descending order.

---

## 4 — Sets (`set` and `frozenset`)

### Properties

* `set`: unordered collection of unique elements; mutable (you can add/remove elements). Elements must be hashable.
* `frozenset`: immutable variant of `set`, hashable itself (so it can be a dict key or element of another set).

### Important nuance (common confusion)

* **Elements are immutable (i.e., each element must be hashable)** — that is why you cannot put a list into a set.
* **But the set object itself is mutable**: you can add/remove elements.

  * Means: "set" as a container is mutable, but its elements must be immutable/hashable.
  * Example: `s = {1,2}; s.add(3)` OK. `s.add([4])` raises `TypeError` because list is not hashable.

### Operations

```python
s = set([1,2,3])
s.add(4)
s.remove(3)       # KeyError if not present
s.discard(10)     # no error if absent
s.pop()           # removes arbitrary element
1 in s            # membership O(1) average
len(s)
```

### Complexity

* Average O(1) for add/remove/membership.

### Edge cases

* Sets are unordered; iteration order unpredictable and may change.
* To get an immutable set: `f = frozenset([1,2,3])`.

---

## 5 — Dictionaries (`dict`)

### Properties

* Mutable, associative mapping of `key -> value`.
* Keys must be hashable (immutable types typically).
* From Python 3.7, insertion order is preserved (practical guarantee).

### Create

```python
d = {'a':1, 'b':2}
d = dict(a=1, b=2)
d = dict([('a',1), ('b',2)])
d = dict(zip(keys, vals))
```

### Access & update

```python
val = d['a']             # KeyError if not present
val = d.get('a')         # None if not present
val = d.get('a', 0)      # default if not present

d['c'] = 3               # adds or updates key
d.update({'x':9})        # update from another dict
d.setdefault('k', 0)    # returns existing or sets default
```

### Removing elements

```python
del d['a']               # KeyError if not present
d.pop('a')               # KeyError if not present
d.pop('a', None)         # returns None if absent — avoids KeyError
```

### Iteration

* `for k in d:` iterates keys.
* `for k, v in d.items():` iterate pairs.
* `for v in d.values():` iterate values.

### Constructing dict from two lists (keys, vals)

```python
mydict = dict(zip(keys, vals))
# or dict(keys=vals) is wrong use-case
# dict(keys, vals) is not valid; but `dict(zip(keys, vals))` is correct.
```

### Identity vs equality note (quiz)

* `==` checks value equality (for lists, tuples, dicts).
* `is` checks identity (same object).

```python
a = [1,2,3]
b = [1,2,3]
a == b    # True
a is b    # False
c = a
a is c    # True
```

---

## 6 — Reversing / inverting a dictionary (swap keys & values)

### Simple (values unique)

```python
org_dict = {'a':1, 'b':2, 'c':3}
rev = {v:k for k,v in org_dict.items()}
# rev -> {1:'a', 2:'b', 3:'c'}
```

Complexity `O(n)`.

### If values are not unique (you must preserve all original keys)

Use list-of-keys per value:

```python
org = {'a':1, 'b':2, 'c':2, 'd':3}
rev = {}
for k, v in org.items():
    if v not in rev:
        rev[v] = [k]
    else:
        rev[v].append(k)
# rev -> {1:['a'], 2:['b','c'], 3:['d']}
```

Or using `collections.defaultdict(list)`:

```python
from collections import defaultdict
rev = defaultdict(list)
for k,v in org.items():
    rev[v].append(k)
```

### Pitfall

If you blindly do `rev_dict[val] = key` and values repeat, later keys overwrite earlier ones — you'll lose data.

---

## 7 — Dictionary inversion problem from quiz (logic used in UI)

When building reversed dictionary where duplicates values exist, UI gave code snippets like:

* `if value not in dict: dict[value] = [key] else: dict[value].append(key)`
  That’s the correct pattern.

---

## 8 — Matrix multiplication (nested loops) — algorithm & code

### Problem

Multiply `A` (m × n) by `B` (n × p) → result `C` (m × p).

### Algorithm (standard triple-loop)

```python
A = [[...], ...]   # m rows
B = [[...], ...]   # n rows, each length p
m = len(A)
n = len(A[0])
p = len(B[0])
C = []
for i in range(m):
    row = []
    for j in range(p):
        s = 0
        for k in range(n):
            s += A[i][k] * B[k][j]
        row.append(s)
    C.append(row)
print(C)
```

### Complexity

* Time `O(m * n * p)` — cubic in matrix dimensions typically.
* Space `O(m*p)` for result.

### Common mistakes in quizzes

* Swapping loops incorrectly or using wrong index ranges.
* Resetting sums incorrectly outside the inner loop.
* Not ensuring `n == len(B)` (compatibility check).

---

## 9 — Grouping data (example: Product sales grouped by city)

### Problem summary (from product sales exercise)

* Input: number of employees `N`.
* For each employee: `name`, `products_sold` (must be non-negative), `city`.
* Requirements: Validate `N > 0`. If invalid: print error and terminate. If any `products_sold` negative: print error and terminate.
* Output: sales grouped by city, listing each employee and their sales.

### Implementation patterns

**Using `dict.setdefault`**

```python
n = int(input(...))
if n <= 0:
    print("Error: Please enter a number greater than zero")
    exit()

groups = {}
for _ in range(n):
    name = input("Enter employee name: ")
    sold = int(input("Enter number of products sold: "))
    if sold < 0:
        print("Error: Sales cannot be negative")
        exit()
    city = input("Enter city: ")

    groups.setdefault(city, []).append((name, sold))

# print grouped
print("Sales Data Grouped by City:")
for city, records in groups.items():
    print("City:", city)
    for name, sold in records:
        print(f" - {name}: {sold} sales")
```

**Using `collections.defaultdict(list)`**

```python
from collections import defaultdict
groups = defaultdict(list)
...
groups[city].append((name, sold))
```

### Edge cases & validation

* Trailing spaces or different capitalization in city names: consider normalizing with `.strip()` and `.title()`/`.lower()` depending on requirement.
* Duplicate names across different cities: allowed.
* Input errors: use try/except for robust parsing.

---

## 10 — Sorting & `sorted()` details

* `sorted(iterable, key=..., reverse=False)` returns a **new list**; does not mutate input.
* `list.sort(key=..., reverse=False)` sorts the list in-place and returns `None`.
* `key` is a function applied to items to decide order, e.g., `key=len` or `key=lambda x: x[1]`.
* Example: sort tuples by string length:

  ```python
  sorted_tuple = tuple(sorted(my_tuple, key=len))
  ```

---

## 11 — `dict` creation options (quiz relevance)

* `dict(zip(keys, vals))` — pair up two lists into a dict.
* `dict.fromkeys(keys, value)` — creates a dict with given keys mapping to same value (careful if value is a mutable object).
* `dict(keys, vals)` is invalid.
* `mydict = dict(keys, vals)` will raise; use `dict(zip(keys, vals))`.

---

## 12 — Identity vs equality & list copies (quiz items)

* `a == b` checks equal content; `a is b` checks same object.
* `b = a` makes `b` reference same object: `a is b` True.
* `b = a.copy()` or `b = list(a)` creates a shallow copy: `a is b` False, `a == b` True.

---

## 13 — Mutability/immutability mixed-language summary (clear answers to quiz-style statements)

* *Dictionaries are key-value paired.* True.
* *Lists are mutable and ordered.* True.
* *Tuples are immutable and ordered.* True.
* *Sets are mutable, elements must be immutable; frozensets are immutable.* True.
* *Tuples are not required to be homogeneous.* False — tuples can contain mixed types.

---

## 14 — `dict[k] = v` when `k` isn't present (quiz question)

* Behavior: **the entry (k, v) is added to the dictionary**. No error.

---

## 15 — Creating inverted dictionaries (step-by-step slide content)

* If values are unique, use comprehension: `{v:k for k,v in org.items()}`
* If values repeat, produce lists per value using `setdefault` or `defaultdict(list)`.

---

## 16 — Useful functions / patterns & best practices

* `defaultdict(list)` simplifies grouping tasks:

  ```python
  from collections import defaultdict
  groups = defaultdict(list)
  groups[city].append((name,sold))
  ```

* `zip(keys, vals)` pairs lists; `dict(zip(keys, vals))` creates dict.

* `pop(key, default)` avoids KeyError.

* `setdefault(key, default)` sets default if key absent and returns value.

* `reversed(dict)`? Not directly—convert keys to list and reverse if needed.

* Avoid using mutable objects (like list/dict) as default values for function parameters.

---

## 17 — Sorting strings by length / example (quiz input)

Example code shown on quiz (fill the blanks):

```python
t = ('apple', 'orange', 'pear')
order = 'desc'

if 'asc' in order:
    st = sorted(t, key=len)
else:
    st = sorted(t, key=len, reverse=True)
print(tuple(st))
```

---

## 18 — Matrix multiplication quiz (how to line up the code blocks)

Canonical ordering for building result `m`:

1. Initialize matrices and result containers:

```python
A = [[1,3], [-5,6], [2,4]]
B = [[1,4], [8,7]]
r = []
m = []
```

2. Outer loop over rows of A:

```python
for i in range(len(A)):
    r = []
    for j in range(len(B[0])):
        sums = 0
        for k in range(len(B)):
            sums = sums + A[i][k] * B[k][j]
        r.append(sums)
    m.append(r)
print(m)
```

(Names may vary; logic is `i` over rows, `j` over columns, `k` for dot product.)

---

## 19 — Multiple-choice truths (from slides)

* `Tuples are immutable, lists are mutable.` — **True**.
* `Dictionaries are indexed` — phrasing ambiguous; dictionaries are keyed (key-value), not index-based with integer indices. So treat statement carefully: "Dictionaries are indexed" often means "key lookup" not positional index.

---

## 20 — Practical error handling & input validation (Product Sales example)

* Validate `employees` input:

```python
try:
    employees = int(input("Enter the number of employees: "))
except ValueError:
    print("Error: Please enter an integer")
    exit()

if employees <= 0:
    print("Error: Please enter a number greater than zero")
    exit()
```

* Validate `products_sold`:

```python
try:
    products = int(input("Enter number of products sold: "))
except ValueError:
    print("Error: please enter an integer")
    exit()

if products < 0:
    print("Error: Sales cannot be negative")
    exit()
```

* Normalization:

  * Use `.strip()` to remove spaces.
  * Use `.title()` or `.lower()` to standardize city names when grouping.

---

## 21 — Edge cases & gotchas summary (be prepared for these in exams)

1. **Dictionary inversion losing keys**: If values repeat and you assign `rev[val] = key`, earlier keys are overwritten.
2. **`del d[k]` vs `d.pop(k, default)`**: `del` and `pop(k)` raise `KeyError` if absent; `pop(k, None)` returns `None`.
3. **Set elements must be hashable**: You cannot do `s.add([1,2])` but can do `s.add((1,2))`.
4. **Mutable default args**: `def f(a=[]):` uses same list across calls.
5. **Iteration order**: Rely on `dict` insertion order only for Python 3.7+ (note exam environment—assume 3.7+ unless told otherwise).
6. **`is` vs `==`**: `is` compares identity (object), `==` value equality.
7. **Sorting returns list**: `sorted()` → list; convert to tuple if required.
8. **Matrix dims mismatch**: Multiply only if columns of A (`n`) == rows of B.
9. **List `index()` returns first occurrence**; using `>` in max logic returns index of first max, not last.

---

## 22 — Quick reference code snippets

### Reverse dictionary (unique values)

```python
org = {'a':1,'b':2,'c':3}
rev = {v:k for k,v in org.items()}
```

### Reverse dictionary (duplicate values)

```python
from collections import defaultdict
rev = defaultdict(list)
for k,v in org.items():
    rev[v].append(k)
# convert to normal dict if wanted:
rev = dict(rev)
```

### Group employees by city

```python
from collections import defaultdict
groups = defaultdict(list)

n = int(input(...))
for _ in range(n):
    name = input().strip()
    sold = int(input().strip())
    city = input().strip()
    groups[city].append((name, sold))
```

### Matrix multiply

```python
def matmul(A,B):
    m, n = len(A), len(A[0])
    assert n == len(B)
    p = len(B[0])
    C = [[0]*p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            s=0
            for k in range(n):
                s += A[i][k]*B[k][j]
            C[i][j] = s
    return C
```

---

## 23 — Short checklist to convert any UI/quiz screenshot into correct answers

* Read the allowed options (some questions reuse same options).
* For code ordering questions: identify outer loop (rows), inner loop (columns), innermost (dot product).
* For dict creation from lists: `dict(zip(keys, vals))` or `dict.fromkeys` (different semantics).
* For identity/equality: remember `a==b` vs `a is b`.
* For set-mutable confusion: remember set container is mutable, elements must be immutable.

---

## 24 — Final compact “cheat sheet” (one-liners)

* `list`: mutable, ordered, indexable.
* `tuple`: immutable, ordered.
* `set`: mutable container, unique elements, elements must be hashable. `frozenset` is immutable set.
* `dict`: mutable mapping of hashable keys to values. `dict.items()` iterates `(k,v)` pairs.
* `sorted(seq, key=..., reverse=...)` returns list.
* `dict(zip(keys, vals))` to build dict from parallel lists.
* `defaultdict(list)` for grouping.
* `pop(k, default)` to avoid KeyError.
* `a == b` → value equality; `a is b` → identity.

---

