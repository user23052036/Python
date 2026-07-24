Yes. This is probably the **simplest brute-force solution** and is a good way to understand the problem before learning the optimized duplicate-skipping approach.

The idea is exactly what you wrote:

```text
Generate all 2^n subsets
        ↓
Store them in a Set
        ↓
Convert the Set back to List<List<int>>
```

Since a Python list is **not hashable**, we store each subset as a **tuple** inside the set.

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(index):
            # Base Case
            if index == len(nums):
                unique_subsets.add(tuple(path))
                return

            # Pick the current element
            path.append(nums[index])
            dfs(index + 1)
            path.pop()

            # Do not pick the current element
            dfs(index + 1)

        nums.sort()              # Optional but keeps duplicate subsets identical
        unique_subsets = set()
        path = []

        dfs(0)

        # Convert tuples back to lists
        ans = []
        for subset in unique_subsets:
            ans.append(list(subset))

        return ans
```

---

# Why does this work?

Suppose

```text
nums = [1,2,2]
```

The recursion **doesn't care** about duplicates.

It generates all

```text
2³ = 8
```

subsets.

The recursion tree is

```text
                         []
                      /        \
                   Pick1      NotPick1
                  /                \
               [1]                  []
             /     \              /     \
         Pick2    Not2       Pick2     Not2
         ...
```

Eventually you'll generate

```text
[]
[1]
[2]
[2]          ← duplicate
[1,2]
[1,2]        ← duplicate
[2,2]
[1,2,2]
```

Notice

```text
[2]
```

appears twice.

Likewise

```text
[1,2]
```

appears twice.

---

## The Set removes duplicates

When you do

```python
unique_subsets.add(tuple(path))
```

the set becomes

```text
{
 (),
 (1,),
 (2,),
 (1,2),
 (2,2),
 (1,2,2)
}
```

The duplicate tuples are automatically ignored because **a set cannot contain the same element twice**.

---

# Why convert to tuple?

Lists are mutable.

```python
[1,2]
```

can become

```python
[1,2,3]
```

Python therefore doesn't allow them inside a set.

```python
set().add([1,2])   ❌ TypeError
```

Tuples are immutable.

```python
(1,2)
```

can never change.

So Python allows

```python
set().add((1,2))   ✅
```

---

# Complexity

```text
Generating all subsets      : O(2^n)

Copying each subset         : O(n)

Total                       : O(n * 2^n)

Set insertion               : Average O(1)

Overall                     : O(n * 2^n)
```

Space:

```text
Recursion stack             : O(n)

Set storing subsets         : O(n * 2^n)
```

---

# Comment you can paste below this solution

```python
# BRUTE FORCE APPROACH
#
# Idea:
# 1. Ignore duplicates while generating subsets.
# 2. Generate ALL 2^n subsets using the standard Pick / Not Pick recursion.
# 3. Store every subset as a tuple inside a set.
# 4. Since a set automatically removes duplicate tuples, only unique subsets remain.
# 5. Convert the tuples back to lists before returning.
#
# Why tuple?
# Python lists are mutable (unhashable), so they cannot be stored in a set.
# Tuples are immutable (hashable), so they can be used as set elements.
#
# This is easy to understand but not optimal because we still generate many
# duplicate subsets. The optimized solution prevents duplicate branches from
# being explored in the first place using:
#
#     if i > start and nums[i] == nums[i-1]:
#         continue
#
# Think of this brute-force solution as:
#
#     Generate Everything  --->  Remove Duplicates Later
#
# and the optimized solution as:
#
#     Never Generate Duplicate Branches in the First Place
```

I actually recommend learning this brute-force version first. It makes the optimized solution feel like a natural improvement rather than a trick. The optimized approach simply moves the duplicate handling **from the end of the algorithm to the recursion itself**.
