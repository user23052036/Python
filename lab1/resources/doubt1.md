Given:

```python
article_title = "data science basics"
```

### 1. `article_title.title()` ✅

Capitalizes the **first letter of every word**.

```python
article_title.title()
# Output: "Data Science Basics"
```

This is the correct answer.

---

### 2. `article_title.capitalize()`

Capitalizes **only the first character of the entire string** and makes the rest lowercase.

```python
article_title.capitalize()
# Output: "Data science basics"
```

Notice only **Data** starts with a capital letter.

---

### 3. `article_title.upper()`

Converts **all letters to uppercase**.

```python
article_title.upper()
# Output: "DATA SCIENCE BASICS"
```

---

### 4. `article_title.proper()`

❌ This method **does not exist** in Python strings.

```python
article_title.proper()
# AttributeError
```

Many people confuse it with Excel's `PROPER()` function, but Python uses `.title()` instead.

### Quick Summary

| Method          | Output                                   |
| --------------- | ---------------------------------------- |
| `.title()`      | `Data Science Basics` ✅                  |
| `.capitalize()` | `Data science basics`                    |
| `.upper()`      | `DATA SCIENCE BASICS`                    |
| `.proper()`     | Error (not a valid Python string method) |

A common exam trap is offering both `.proper()` and `.title()`. In Python, always choose **`.title()`**.


---

The **correct answer is:**

```python
"C:\\Users\\name\\Documents"
```

### Why?

In Python strings, the backslash `\` is an **escape character**.

Examples:

```python
"\n"   # newline
"\t"   # tab
"\""   # double quote
```

So if you want an actual backslash in the string, you must write it as `\\`.

---

## Option 1 ✅

```python
"C:\\Users\\name\\Documents"
```

Each `\\` becomes a single `\` when Python interprets the string.

Actual value:

```text
C:\Users\name\Documents
```

Correct.

---

## Option 2 ❌

```python
'C:\Users\name\Documents'
```

Problem:

Python sees:

```python
\U
\n
```

* `\n` = newline
* `\U` starts a Unicode escape sequence

This can produce errors or unexpected results.

Example:

```python
'C:\new'
```

becomes

```text
C:
ew
```

because `\n` is interpreted as a newline.

---

## Option 3 ✅ (but not what the question is asking)

```python
"C:/Users/name/Documents"
```

Forward slashes are actually accepted by Python and Windows.

```python
open("C:/Users/name/Documents/file.txt")
```

often works fine.

However, the question specifically asks for the path:

```text
C:\Users\name\Documents
```

so the exact representation is Option 1.

---

## Option 4 ❌

```python
"C:\Users\name\Documents"
```

Same problem as Option 2.

Python interprets sequences like:

```python
\U
\n
```

as escape sequences rather than literal backslashes.

---

### Another valid Python way

Using a **raw string**:

```python
r"C:\Users\name\Documents"
```

The `r` tells Python not to treat backslashes as escape characters.

This is often the preferred way to write Windows paths.

### Summary

| Option                         | Valid? | Reason                                             |
| ------------------------------ | ------ | -------------------------------------------------- |
| `"C:\\Users\\name\\Documents"` | ✅      | Escaped backslashes                                |
| `'C:\Users\name\Documents'`    | ❌      | `\U`, `\n` treated as escapes                      |
| `"C:/Users/name/Documents"`    | ✅      | Valid path, but not the exact backslash form asked |
| `"C:\Users\name\Documents"`    | ❌      | Escape-sequence issue                              |
| `r"C:\Users\name\Documents"`   | ✅      | Raw string (best practice)                         |


---
