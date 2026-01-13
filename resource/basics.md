
## **1. `.isalpha()`**

Think of it as a **built-in question** you ask a string:

> “Hey, are you made of ONLY alphabet letters?”

If yes → returns `True`
If no → returns `False`

Examples:

```
"a".isalpha()    → True
"Z".isalpha()    → True
"abc".isalpha()  → True
"7".isalpha()    → False
"@" .isalpha()   → False
"hi!" .isalpha() → False
```

So `.isalpha()` = **is alphabetic** (letters only).

---

### 🔹 Why is it named like this?

Python uses short, readable, English-based names:

`is`  → asking a Yes/No question
`alpha` → refers to alphabet characters (A–Z)

Together = **is-alpha**.

---

### 🔹 Other similar checks (and why they are named that way)

Python gives many `.isXXX()` functions to check the nature of input.

| Method       | Meaning                          | Why named like that            |
| ------------ | -------------------------------- | ------------------------------ |
| `.isdigit()` | Checks if string has only digits | digit = number character       |
| `.isalnum()` | Letters or digits allowed        | alphanumeric = alpha + numeric |
| `.islower()` | Checks if letters are lowercase  | lower = small letters          |
| `.isupper()` | Checks uppercase                 | upper = capital letters        |
| `.isspace()` | Only whitespace characters       | space = blank characters       |

Example:

```
"abc".isdigit() → False
"123".isdigit() → True
"abc123".isalnum() → True
```

Each follows the same pattern:

👉 `is` (question) + meaning (alpha, digit, lower, upper)


<br>
<br>

## **2. `if(__name__ == "__main__"):`**

`if __name__ == "__main__":` checks if the Python file is being run directly. When run directly, `__name__` is `"__main__"`, so the code in this block executes. When the same file is imported into another program, `__name__` becomes the module’s filename instead of `"__main__"`, so the block is skipped. This lets you write reusable functions while keeping main/test code from running on import.

<br>
<br>
