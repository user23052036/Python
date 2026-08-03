Yes. The **pick/not-pick recursion pattern is fundamentally the same** for both **printing all subsequences** and **generating all subsets**. The only real difference is the terminology and sometimes the input constraints.

### Generic Pick/Not Pick Template

```python
def backtrack(index):
    if index == n:
        print(current)
        return

    # Pick
    current.append(arr[index])
    backtrack(index + 1)
    current.pop()

    # Not Pick
    backtrack(index + 1)
```

---

## 1. Printing All Subsequences

For an array:

```python
arr = [1, 2, 3]
```

Output:

```
[1,2,3]
[1,2]
[1,3]
[1]
[2,3]
[2]
[3]
[]
```

Every element has two choices:

* Include it
* Exclude it

Exactly the code above.

---

## 2. Generating All Subsets (LeetCode 78)

The code is literally identical.

```python
class Solution:
    def subsets(self, nums):

        result = []
        current = []

        def backtrack(index):

            if index == len(nums):
                result.append(current[:])
                return

            # Pick
            current.append(nums[index])
            backtrack(index + 1)
            current.pop()

            # Not Pick
            backtrack(index + 1)

        backtrack(0)
        return result
```

This is exactly the subsequence algorithm.

---

## Why are they the same?

A **subset** of an array is simply a **subsequence where order is preserved**.

For arrays with **distinct elements**:

```
Subsequences == Subsets
```

Example:

```
[1,2,3]
```

Both produce

```
[]
[1]
[2]
[3]
[1,2]
[1,3]
[2,3]
[1,2,3]
```

---

## Then why are there two names?

Because they are used in different contexts.

### Subsequence

* Sequence problems
* Dynamic Programming
* Order matters
* Usually discussed with strings

Example:

```
ABC

Subsequence:
A
B
C
AB
AC
BC
ABC
```

Notice `"BA"` is **not** a subsequence because the original order must be preserved.

---

### Subset

* Set problems
* Backtracking
* Combination generation
* Mathematical terminology

Example:

```
{1,2,3}

Subsets:
{}
{1}
{2}
{3}
{1,2}
{1,3}
{2,3}
{1,2,3}
```

The implementation over an array still preserves the original order, so the generated lists match the subsequences.

---

## When do they become different?

If the array contains duplicates.

Example:

```
nums = [1,2,2]
```

Naive pick/not-pick gives duplicate outputs:

```
[]
[2]
[2]      <- duplicate
[1,2]
[1,2]    <- duplicate
...
```

For **Subsets II (LeetCode 90)**, you need extra logic (sorting and skipping duplicates).

---

### Rule to remember

* **Subsequence = Pick / Not Pick**
* **Subset = Pick / Not Pick**
* **Subset II = Pick / Not Pick + Skip duplicates**
* **Combination Sum = Pick / Not Pick** (with modified recursive calls depending on whether elements can be reused)

So yes—the recursive structure for printing all subsequences and generating all subsets is the same. The difference is primarily the problem's interpretation and any additional constraints such as duplicate handling.
