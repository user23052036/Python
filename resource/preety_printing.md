
### 1. `__str__` (The User-Friendly View)

This is called when an object needs to be "pretty-printed" for an end-user.

* **Triggered by:** `print(obj)`, `str(obj)`, or f-string interpolation `f"{obj}"`.
* **Internal Goal:** Provide a readable, informal representation of the object.
* **Fallback:** If `__str__` is not defined, Python will look for `__repr__` instead.

### 2. `__repr__` (The Developer View)

Short for "representation," this is used for debugging and development.

* **Triggered by:** Typing the variable name in a REPL (like Jupyter or IDLE), `repr(obj)`, or when the object is inside a collection (e.g., `print([obj1, obj2])`).
* **Internal Goal:** Provide an unambiguous representation. Ideally, the output should look like the Python code used to create the object (e.g., `Fraction(1, 2)`).
* **Unique Role:** This is the ultimate fallback. Every object has a default `__repr__` (usually showing the memory address) even if you don't define one.

---

### Internal Execution Flow

| Scenario | Primary Method Called | Secondary (Fallback) |
| --- | --- | --- |
| `print(obj)` | `obj.__str__()` | `obj.__repr__()` |
| `str(obj)` | `obj.__str__()` | `obj.__repr__()` |
| `repr(obj)` | `obj.__repr__()` | (None) |
| Inspecting in Console | `obj.__repr__()` | (None) |
| `print([obj])` | `obj.__repr__()` | (None) |

### Practical Example

If you have a `Fraction` class:

* `__str__` might return `"1/2"` (easy for a human to read).
* `__repr__` might return `"Fraction(1, 2)"` (clear to a developer exactly what the object is).
