
# 1. How Java Method Overloading Works

In Java, **multiple methods with the same name can coexist** if their **parameter signatures differ**.

Example:

```java
class MathUtil {

    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
}
```

Compiler decides **which method to call at compile time** based on:

* number of parameters
* parameter types
* parameter order

This is **compile-time polymorphism**.

---

# 2. What Happens in Python

Python does **not store multiple functions with the same name**.

If you define:

```python
class Test:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
```

The second definition **overwrites the first one**.

So effectively Python keeps only:

```python
def add(self, a, b, c):
    return a + b + c
```

The first method is **lost**.

This happens because Python:

* executes code **top → bottom**
* stores functions in a **dictionary (`__dict__`)**
* same key (`add`) gets replaced

---

# 3. How Python Achieves Similar Behavior

Python solves the same problem using **different mechanisms**.

## Method 1 — Default Arguments

```python
def add(a, b, c=None):
    if c is None:
        return a + b
    return a + b + c
```

Usage:

```
add(2,3)
add(2,3,4)
```

---

## Method 2 — *args (Most Pythonic)

```python
def add(*nums):
    return sum(nums)
```

Usage:

```
add(2,3)
add(2,3,4)
add(1,2,3,4,5)
```

---

## Method 3 — Type Based Dispatch (Closest to Java)

Python 3.4+ provides:

```
functools.singledispatch
```

Example:

```python
from functools import singledispatch

@singledispatch
def fun(x):
    print("Default")

@fun.register
def _(x: int):
    print("Integer")

@fun.register
def _(x: str):
    print("String")
```

Now:

```
fun(10)  → Integer
fun("hi") → String
```

---

# 4. Why Python Does Not Need Method Overloading

Python philosophy:

```
"One flexible function > many overloaded functions"
```

Because Python has:

* dynamic typing
* default parameters
* *args
* **kwargs

So Java-style overloading becomes **unnecessary complexity**.

---

# 5. The Real Interview Answer

If someone asks:

**Does Python support method overloading?**

Correct answer:

> Python does not support traditional compile-time method overloading like Java. If multiple methods with the same name are defined, the last one overwrites the previous definitions. Similar behavior can be achieved using default parameters, *args, or function dispatch mechanisms.

---

# One More Important Detail (Most People Miss)

Python **does support operator overloading**.

Example:

```python
class Vector:

    def __add__(self, other):
        return "Vector addition"
```

So:

```
v1 + v2
```

calls

```
v1.__add__(v2)
```

---
