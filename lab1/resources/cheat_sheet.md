# Python Basics Cheatsheet

## Comments
Lines of text ignored by the Python interpreter during execution. Used for explanations and notes.

```python
# This is a single-line comment

"""
This is a
multi-line comment (docstring style)
"""
```

---

## Data Types
Python's core built-in data types.

| Type | Example |
|------|---------|
| Integer | `x = 7` |
| Float | `y = 12.4` |
| Boolean | `is_valid = True` |
| String | `F_Name = "John"` |
| List | `fruits = ["apple", "banana"]` |
| Tuple | `coords = (10, 20)` |
| Dictionary | `person = {"name": "John", "age": 25}` |
| Set | `unique_nums = {1, 2, 3}` |
| NoneType | `result = None` |

```python
x = 7            # Integer
y = 12.4         # Float
is_valid = True  # Boolean
F_Name = "John"  # String
```

---

## Variable Assignment
Assigns a value to a variable.

**Syntax:**
```python
variable_name = value
```

**Example:**
```python
name = "John"  # assigning "John" to variable name
x = 5           # assigning 5 to variable x

# Multiple assignment
a, b, c = 1, 2, 3
```

---

## Python Operators

| Operator | Name | Description |
|----------|------|-------------|
| `+` | Addition | Adds two values together |
| `-` | Subtraction | Subtracts one value from another |
| `*` | Multiplication | Multiplies two values |
| `/` | Division | Divides one value by another, returns a float |
| `//` | Floor Division | Divides and returns the quotient as an integer |
| `%` | Modulo | Returns the remainder after division |
| `**` | Exponent | Raises a number to a power |

```python
x = 9
y = 4

result_add  = x + y   # Addition       -> 13
result_sub  = x - y   # Subtraction    -> 5
result_mul  = x * y   # Multiplication -> 36
result_div  = x / y   # Division       -> 2.25
result_fdiv = x // y  # Floor Division -> 2
result_mod  = x % y   # Modulo         -> 1
result_exp  = x ** y  # Exponent       -> 6561
```

### Comparison Operators
`==`, `!=`, `>`, `<`, `>=`, `<=` — return `True` or `False`

```python
print(x == y)  # False
print(x > y)   # True
```

### Logical Operators
`and`, `or`, `not`

```python
print(x > 5 and y < 10)  # True
print(x > 5 or y > 10)   # True
print(not is_valid)      # negates the boolean
```

---

## print()
Prints the message or variable inside `()`.

```python
print("Hello, world")
print(a + b)
print("Sum is:", a + b)
print(f"Sum is: {a + b}")  # f-string formatting
```

---

## String Operations

### Concatenation
Combines (joins) strings together using `+`.

**Syntax:**
```python
concatenated_string = string1 + string2
```

**Example:**
```python
result = "Hello" + " John"
print(result)  # Hello John
```

### Indexing
Accesses the character at a specific index (0-based; negative indices count from the end).

```python
my_string = "Hello"
char = my_string[0]   # 'H'
last = my_string[-1]  # 'o'
```

### Slicing
Extracts a portion (substring) of a string.

**Syntax:**
```python
substring = string_name[start:end]
```

**Example:**
```python
my_string = "Hello"
substring = my_string[0:3]  # 'Hel'
substring2 = my_string[::-1]  # 'olleH' (reversed)
```

### len()
Returns the length of a string (or any sequence).

**Syntax:**
```python
len(string_name)
```

**Example:**
```python
my_string = "Hello"
length = len(my_string)  # 5
```

### upper()
Converts a string to uppercase.

```python
my_string = "Hello"
uppercase_text = my_string.upper()  # 'HELLO'
```

### lower()
Converts a string to lowercase.

```python
my_string = "Hello"
lowercase_text = my_string.lower()  # 'hello'
```

### strip()
Removes leading and trailing whitespace.

```python
my_string = "  Hello  "
trimmed = my_string.strip()  # 'Hello'
```

### replace()
Replaces occurrences of a substring with another substring.

```python
my_string = "Hello"
new_text = my_string.replace("Hello", "Hi")  # 'Hi'
```

### split()
Splits a string into a list based on a delimiter.

```python
my_string = "apple,banana,cherry"
split_text = my_string.split(",")  # ['apple', 'banana', 'cherry']
```

### join()
Joins a list of strings into one string using a separator.

```python
words = ["Hello", "World"]
joined = " ".join(words)  # 'Hello World'
```

---

## Conditional Statements
Control the flow of execution based on conditions.

```python
age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

---

## Loops

### for loop
Iterates over a sequence (list, string, range, etc.).

```python
for i in range(5):
    print(i)  # 0 1 2 3 4

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

### while loop
Repeats as long as a condition is `True`.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### break and continue
```python
for i in range(10):
    if i == 5:
        break       # exits the loop entirely
    if i % 2 == 0:
        continue    # skips to the next iteration
    print(i)
```

---

## Lists
Ordered, mutable collections of items.

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")     # add to end
fruits.remove("banana")     # remove by value
fruits.insert(1, "mango")   # insert at index
fruits.pop()                # remove last item
fruits.sort()               # sort in place
print(len(fruits))          # length of list
print(fruits[0])            # access by index
print(fruits[1:3])          # slicing
```

---

## Tuples
Ordered, **immutable** collections of items.

```python
coords = (10, 20)
x, y = coords  # unpacking
print(coords[0])  # 10
```

---

## Dictionaries
Key-value pairs.

```python
person = {"name": "John", "age": 25}

print(person["name"])       # access value
person["age"] = 26          # update value
person["city"] = "NYC"      # add new key-value pair
del person["city"]          # remove key

for key, value in person.items():
    print(key, value)
```

---

## Sets
Unordered collections of unique items.

```python
unique_nums = {1, 2, 3, 2, 1}  # {1, 2, 3}
unique_nums.add(4)
unique_nums.remove(1)
```

---

## Functions
Reusable blocks of code.

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("John")
print(message)  # Hello, John!

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # 9
print(power(3, 3))  # 27
```

---

## Error Handling
Handles exceptions gracefully using `try`/`except`.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always runs")
```

---

## Type Conversion
Convert between data types.

```python
str_num = "10"
num = int(str_num)        # string to int
float_num = float(num)    # int to float
str_again = str(num)      # int to string
bool_val = bool(0)         # False (0 is falsy)
```

---

## Importing Modules
Use built-in or external libraries.

```python
import math
print(math.sqrt(16))  # 4.0

from datetime import datetime
print(datetime.now())
```

---

## Useful Built-in Functions

| Function | Description | Example |
|----------|-------------|---------|
| `type()` | Returns the data type of a variable | `type(5)` -> `<class 'int'>` |
| `range()` | Generates a sequence of numbers | `range(0, 5)` |
| `sorted()` | Returns a sorted list | `sorted([3, 1, 2])` -> `[1, 2, 3]` |
| `max()` / `min()` | Returns largest/smallest value | `max(1, 2, 3)` -> `3` |
| `sum()` | Returns sum of an iterable | `sum([1, 2, 3])` -> `6` |
| `input()` | Takes user input as a string | `name = input("Enter name: ")` |