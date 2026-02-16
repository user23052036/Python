Both work, but they behave differently.

---

### 1️⃣ Comma Version

```python
print('Hello,', customer.name, 'mam')
```

* `print()` accepts multiple arguments.
* It automatically converts non-strings to string.
* It inserts a space between them by default (`sep=' '`).

Internally:

```python
print(arg1, arg2, arg3, sep=' ')
```

Safer. Cleaner. No manual conversion needed.

---

### 2️⃣ Plus (`+`) Version

```python
print('Hello, ' + customer.name + ' sir')
```

* `+` is string concatenation.
* All operands must be strings.
* If `customer.name` is not a string → `TypeError`.

Example failure:

```python
customer.name = 25
# TypeError: can only concatenate str (not "int") to str
```

---

### Which Is Better?

For simple prints → comma is safer.

For formatting → use f-strings (best practice):

```python
print(f"Hello, {customer.name} sir")
```

Cleaner, safer, more readable.

---

Minimal rule:

* `,` → multiple arguments (automatic spacing)
* `+` → string concatenation (strict type matching)
* `f""` → modern and preferred method
