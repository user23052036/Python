This is a **matching question**. Let’s map each concept correctly.

Available options:

* `__init__.py`
* `import, from`
* `str(), len()`
* `__doc__, return`

---

# Correct Matching

### Built-in functions

These are Python’s predefined functions.

**Answer**

```
str(), len()
```

---

### Package

A package in Python is identified by the file:

**Answer**

```
__init__.py
```

This file tells Python the folder should be treated as a **package**.

---

### Function

Functions typically involve documentation and returning values.

**Answer**

```
__doc__, return
```

* `__doc__` → function documentation string
* `return` → returns value from a function

---

### Modules

Modules are used through importing.

**Answer**

```
import, from
```

Example:

```python
import math
from math import sqrt
```

---

# Final selections

| Item               | Answer            |
| ------------------ | ----------------- |
| Built-in functions | `str(), len()`    |
| Package            | `__init__.py`     |
| Function           | `__doc__, return` |
| Modules            | `import, from`    |

---

First understand the logic they want:

Goal: **add only odd numbers** from the list.

Odd number condition:

```
n % 2 == 1
```

Example given:

```
[1, 4, 8, 9]
odd numbers → 1, 9
sum → 10
```

---

# Available tokens

```
n
sum
numbers
n%2
0
```

---

# Fill the blanks

### 1️⃣

```
sum = 0
```

### 2️⃣

```
for n in numbers
```

### 3️⃣

```
if n % 2 == 1
```

### 4️⃣

```
sum = sum + n
```

### 5️⃣

```
return sum
```

---

# Final filled function

```python
def addOddNumbers(numbers):
    sum = 0
    for n in numbers:
        if n % 2 == 1:
            sum = sum + n
    return sum
```

---

# Verify

```
addOddNumbers([1,4,8,9])
```

```
1 + 9 = 10
```

---

# One important note (good Python practice)

Using `sum` as a variable **overwrites the built-in `sum()` function**.

Better style would be:

```python
total = 0
```

But exams often ignore this.

---

You must construct the function logically. The goal:

Check if **each character is ≤ the next character**.
If any character is **greater than the next**, the word is **not in alphabetical order**.

Example:

```
app → a ≤ p ≤ p → True
apple → p > l → False
```

---

# Correct order of the blocks

1️⃣

```
def isInAlphabeticalOrder(word):
```

2️⃣

```
result = True
```

3️⃣

```
for i in range(0, len(word)-1):
```

4️⃣

```
if word[i] > word[i+1]:
```

5️⃣

```
result = False
```

6️⃣

```
break
```

7️⃣

```
return result
```

---

# Final code (for clarity)

```python
def isInAlphabeticalOrder(word):

    result = True

    for i in range(0, len(word)-1):
        if word[i] > word[i+1]:
            result = False
            break

    return result
```

---

# Quick verification

```
isInAlphabeticalOrder("app")   → True
isInAlphabeticalOrder("apple") → False
```

---

# Important observation (what the exam tests)

They want you to understand:

```
word[i] > word[i+1]
```

means **alphabetical order is violated**.

---

# Faster Pythonic solution (what good programmers write)

```python
def isInAlphabeticalOrder(word):
    return all(word[i] <= word[i+1] for i in range(len(word)-1))
```

But exams almost always expect the **loop version**.

---

This question is asking you to **complete an LCM implementation**.
Let’s reason from the algorithm instead of guessing the dropdown.

### How the algorithm works

To compute LCM of two numbers:

1. Start from the **larger number** (`greater`)
2. Check if it is divisible by **both numbers**
3. If not, **increment** and try again.

So the structure should logically be:

```python
def lm(a, b):

    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lm = greater
            break
        greater += 1

    return lm
```

For multiple numbers, they want to use **reduce**:

```python
def LCM(nums):
    return reduce(lambda x, y: lm(x, y), nums)
```

---

# Correct dropdown selections (in order)

### 1️⃣ After `if a > b`

```
greater = a
```

### 2️⃣ After `else`

```
greater = b
```

### 3️⃣ In the condition

```
greater % a == 0
```

(full condition becomes)

```
if greater % a == 0 and greater % b == 0
```

### 4️⃣ After `break`

```
greater += 1
```

### 5️⃣ Final return in `LCM(nums)`

```
reduce(lambda x, y: lm(x, y), nums)
```

---

# Final filled code

```python
from functools import reduce

def lm(a, b):

    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lm = greater
            break
        greater += 1

    return lm

def LCM(nums):
    return reduce(lambda x, y: lm(x, y), nums)
```

---

# Example

```
LCM([2,3,4]) → 12
LCM([3,3]) → 3
```

---

### Important interview detail

The **real optimal LCM formula** is:

```
LCM(a,b) = abs(a*b) / gcd(a,b)
```

The quiz uses a **brute-force approach**, which is inefficient.

Time complexity here can be **O(LCM)**, which becomes terrible for large numbers.

---

### Question 6

**Identify which function creates a symbolic link**

Options shown:

* `os.symblin()`
* `os.symb_link()`
* `os.ln()`
* `os.symlink()`

Correct answer:

**`os.symlink()`**

Example:

```python
import os
os.symlink("target_file", "link_name")
```

Creates a symbolic link similar to Linux:

```
ln -s target_file link_name
```

---

# Question 7

**Which function reads data from a file using a file descriptor?**

Options:

* `os.quick_read()`
* `os.reader()`
* `os.read()`
* `os.scan()`

Correct answer:

**`os.read()`**

Example:

```python
import os

fd = os.open("file.txt", os.O_RDONLY)
data = os.read(fd, 100)
```

Here `fd` is a **file descriptor**.

---

# Question 8

**What does `os.name` contain?**

Options include:

* address of module
* name of OS dependent module
* error because it should be `os.name()`

Correct answer:

**the name of the operating system dependent module imported**

Example:

```python
import os
print(os.name)
```

Outputs something like:

```
posix
```

or

```
nt
```

---

# Question 9

**What does `print(os.geteuid())` print?**

Options:

* user id of current process
* both group id and user id
* group id

Correct answer:

**the user id of the current process**

Explanation:

`geteuid()` = **effective user ID**

Example on Linux:

```
1000
```

Note: Works only on **Unix-like systems**.

---

# Question 10

**What does `os.close(f)` do?**

Options include:

* return integer
* terminate process
* close file descriptor

Correct answer:

**closes the file descriptor `f`**

Example:

```python
import os

fd = os.open("file.txt", os.O_RDONLY)
os.close(fd)
```

---

# Final Answers

| Question | Answer                                                     |
| -------- | ---------------------------------------------------------- |
| Q6       | `os.symlink()`                                             |
| Q7       | `os.read()`                                                |
| Q8       | the name of the operating system dependent module imported |
| Q9       | the user id of the current process                         |
| Q10      | closes the file descriptor f                               |

---

Quick observation: this quiz is testing **Python `os` module system calls**, basically wrappers over **Unix kernel syscalls** (read, close, uid, symlink). This is closer to **systems programming** than typical Python scripting.

---

Let's go one by one.

---

# Question 3

**Question:**
Which method returns the present working directory?

Options:

* `os.getcwd()`
* `os.getpwd()`
* `os.cwd()`
* `os.pwd()`

### Correct answer

`os.getcwd()`

Explanation:

```python
import os
os.getcwd()
```

returns something like:

```
'/home/user/project'
```

The other options **do not exist in Python's `os` module**.

---

# Question 4

**Question:**
Describe the process of pickling in Python.

Options include:

1. conversion of a Python object hierarchy into byte stream
2. conversion of a list into a data table
3. conversion of a byte stream into Python object hierarchy
4. conversion of a data table into a list

### Correct answer

**conversion of a Python object hierarchy into byte stream**

Explanation:

Pickling = **Serialization**

```
Python object → byte stream
```

Used when storing objects to files or sending over network.

Example:

```python
import pickle

data = {"a":1, "b":2}

with open("data.pkl","wb") as f:
    pickle.dump(data,f)
```

Reverse process:

```
byte stream → Python object
```

is called **Unpickling**.

---

# Question 5

Code:

```python
numbers = [-2,4,6,-1]

new_no = list(filter(lambda x: x > 0, numbers))
```

### Step-by-step

`filter()` keeps elements where the condition is **True**.

Condition:

```
x > 0
```

So only **positive numbers remain**.

Input:

```
[-2,4,6,-1]
```

Result:

```
[4,6]
```

### Correct answer

**It will filter the positive numbers from a list**

---

# Final Answers

| Question | Answer                                                   |
| -------- | -------------------------------------------------------- |
| Q3       | `os.getcwd()`                                            |
| Q4       | conversion of a Python object hierarchy into byte stream |
| Q5       | It will filter the positive numbers from a list          |

---

If you're studying Python deeply (which you should if you're doing ML + interviews), you should also know **why `filter()` returns an iterator in Python 3** and why `list()` is needed. That detail shows up in interviews.

---

Look carefully. The key issue is **Python's argument passing + list mutability**.

### Code

```python
def addItem(listParam):
    listParam += [1]

mylist = [1, 2, 3, 4]
addItem(mylist)
print(len(mylist))
```

---

# Step-by-step reasoning

### 1. Initial list

```python
mylist = [1,2,3,4]
```

Length = **4**

---

### 2. Function call

```python
addItem(mylist)
```

Inside the function:

```python
listParam += [1]
```

Important rule:

* `+=` on a **list performs in-place modification**
* It behaves like:

```python
listParam.extend([1])
```

So the **same list object is modified**.

---

### 3. After modification

The original list becomes:

```python
[1,2,3,4,1]
```

Because lists are **mutable and passed by reference to the object**.

---

### 4. Length calculation

```python
print(len(mylist))
```

Length = **5**

---

# Correct answer

**5**

---

# Why this question exists (interview trap)

If the code was:

```python
listParam = listParam + [1]
```

Then a **new list would be created**, and the original list would stay unchanged.

Output would be **4**.

---

# The core concept they are testing

Python parameter passing:

| Type                        | Behavior                      |
| --------------------------- | ----------------------------- |
| Immutable (int, str, tuple) | new object created            |
| Mutable (list, dict, set)   | modifications affect original |

---

If you're preparing for interviews (which you mentioned earlier), I strongly recommend mastering **three Python mutation traps**:

1. `list * n` aliasing bug
2. `+=` vs `+` with lists
3. default mutable arguments

These three alone eliminate **80% of Python trick questions**.

---

Your instinct should immediately question **line 1**:

```python
list = [[]] * 5
```

This is **not creating 5 independent lists**.
It creates **one list object and 5 references to the same object**.

Memory model:

```
      +----+
list →| *  |----→ []
      | *  |----→ (same list)
      | *  |----→ (same list)
      | *  |----→ (same list)
      | *  |----→ (same list)
      +----+
```

So any modification to one inner list affects **all of them**.

---

# Step-by-step execution

## Line 1

```python
list = [[]] * 5
```

Result:

```
[[], [], [], [], []]
```

But remember: **all refer to the same list object**.

---

# Line 2 output

```python
list
```

```
[[], [], [], [], []]
```

---

# Line 3

```python
list[0].append(10)
```

Because all elements reference the **same list**, every position now shows `[10]`.

---

# Line 4 output

```
[[10], [10], [10], [10], [10]]
```

---

# Line 5

```python
list[1].append(20)
```

Again modifying the **same shared list**.

Now the underlying list becomes:

```
[10, 20]
```

---

# Line 6 output

```
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
```

---

# Line 7

```python
list.append(30)
```

This **adds a new element to the outer list**, not the inner one.

---

# Line 8 output

```
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
```

---

# Final Answer (lines 2,4,6,8)

```
[[], [], [], [], []]

[[10], [10], [10], [10], [10]]

[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]

[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
```

This corresponds to **Option 3**.

---

# The interview trap

If you actually wanted **independent lists**, you must write:

```python
list = [[] for _ in range(5)]
```

Now memory looks like:

```
[ [], [], [], [], [] ]
   ↑   ↑   ↑   ↑   ↑
 different objects
```

Then modifying one index won't affect others.

---

# Brutal interview question they often ask

Predict this:

```python
a = [[]] * 3
a[0] = [1]
print(a)
```

Most people answer wrong.

---

