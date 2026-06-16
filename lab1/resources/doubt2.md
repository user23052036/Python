`append()` adds **one item** to a list, even if that item is another list.

```python
A = [1]
A.append([2, 3, 4, 5])
# A becomes: [1, [2, 3, 4, 5]]
# length = 2
```

To add elements **individually**, use `extend()`:

```python
A = [1]
A.extend([2, 3, 4, 5])
# A becomes: [1, 2, 3, 4, 5]
# length = 5
```

You cannot write:

```python
A.extend(1,2,3,4,5)
```

because `extend()` takes **only one iterable argument**.

Correct examples:

```python
A.extend([1,2,3,4,5])
A.extend((1,2,3,4,5))
A.extend(range(1,6))
```

Also, this works like `extend()`:

```python
A += [2, 3, 4, 5]
```
