This is a very good question, and it's something many students realize too late.

You're learning **algorithm implementation** on LeetCode, but in placements (OA rounds on HackerRank, CodeChef, Codeforces, TCS, Accenture, Cognizant, etc.), you're expected to write the **entire program**:

* Read input
* Process it
* Print output

These are two different skills.

---

# First understand the difference

## LeetCode

You only write

```python
class Solution:
    def twoSum(self, nums, target):
        ...
```

LeetCode secretly does something like

```python
nums = [2,7,11,15]
target = 9

obj = Solution()
print(obj.twoSum(nums, target))
```

You never see the input.

---

## Placement OA

You write everything.

For example

Input

```
4
2 7 11 15
9
```

Your program must

```python
n = int(input())

nums = list(map(int, input().split()))

target = int(input())

# process

print(answer)
```

No one does anything for you.

---

# Step 1 : Reading a single integer

Input

```
5
```

Code

```python
n = int(input())
```

Explanation

```
input()

returns string

↓

"5"

↓

int()

↓

5
```

Always remember

```
input()

always returns string.
```

---

# Step 2 : Reading a string

Input

```
hello
```

```python
s = input()
```

Output

```
hello
```

No conversion needed.

---

# Step 3 : Reading two integers

Input

```
10 20
```

Code

```python
a, b = map(int, input().split())
```

Let's understand this.

---

## First

```python
input()
```

returns

```
"10 20"
```

---

Then

```python
.split()
```

breaks at spaces

```
["10", "20"]
```

---

Then

```python
map(int, ...)
```

converts every string into integer

```
10
20
```

---

Finally

```python
a, b = ...
```

stores

```
a = 10
b = 20
```

---

# Step 4 : Reading a list

Input

```
1 2 3 4 5
```

Code

```python
arr = list(map(int, input().split()))
```

Let's break it down.

```
input()

↓

"1 2 3 4 5"

↓

split()

↓

["1","2","3","4","5"]

↓

map(int,...)

↓

1 2 3 4 5

↓

list()

↓

[1,2,3,4,5]
```

Now

```
arr

=

[1,2,3,4,5]
```

---

# Step 5 : Reading n numbers

Input

```
5
1 2 3 4 5
```

Code

```python
n = int(input())

arr = list(map(int, input().split()))
```

Here

```
n = 5

arr = [1,2,3,4,5]
```

Sometimes people do

```python
assert len(arr) == n
```

just to verify.

---

# Step 6 : Reading multiple lines

Input

```
3
5
8
10
```

Code

```python
n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))
```

Result

```
[5,8,10]
```

---

# Step 7 : Reading matrix

Input

```
3 4

1 2 3 4
5 6 7 8
9 10 11 12
```

Code

```python
rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))
```

Result

```
[
 [1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]
]
```

---

# Step 8 : Reading test cases

Very common in placements.

Input

```
3
5
7
10
```

Meaning

There are

```
3 test cases
```

Code

```python
t = int(input())

for _ in range(t):
    n = int(input())

    print(n*n)
```

Output

```
25
49
100
```

---

# Another example

Input

```
2

5
1 2 3 4 5

4
9 8 7 6
```

Code

```python
t = int(input())

for _ in range(t):

    n = int(input())

    arr = list(map(int, input().split()))

    print(sum(arr))
```

---

# Step 9 : Reading characters

Input

```
abcd
```

Code

```python
s = input()

chars = list(s)
```

Result

```
['a','b','c','d']
```

---

# Step 10 : Reading digits

Input

```
12345
```

Code

```python
digits = list(map(int, input()))
```

Result

```
[1,2,3,4,5]
```

Notice

There is **NO**

```
split()
```

because every character is already separate.

---

# Step 11 : Printing output

Single value

```python
print(ans)
```

---

List

```python
print(arr)
```

prints

```
[1, 2, 3]
```

Many judges **do not** want brackets.

Instead

```python
print(*arr)
```

Output

```
1 2 3
```

This is very common.

---

Print one per line

```python
for x in arr:
    print(x)
```

Output

```
1
2
3
```

---

# Step 12 : Printing matrix

```python
for row in matrix:
    print(*row)
```

Output

```
1 2 3
4 5 6
7 8 9
```

---

# Step 13 : Fast input (important)

For very large inputs (common in Codeforces and some OAs), `input()` can become slow.

Use

```python
import sys

input = sys.stdin.readline
```

Now everything else remains the same.

```python
n = int(input())

arr = list(map(int, input().split()))
```

The only difference is that `sys.stdin.readline()` keeps the trailing newline (`\n`), but `int()`, `split()`, and `strip()` handle it naturally.

---

# Step 14 : Common patterns you should memorize

## One integer

```python
n = int(input())
```

---

## Two integers

```python
a, b = map(int, input().split())
```

---

## Three integers

```python
a, b, c = map(int, input().split())
```

---

## List

```python
arr = list(map(int, input().split()))
```

---

## String

```python
s = input()
```

---

## Matrix

```python
matrix = [list(map(int, input().split())) for _ in range(n)]
```

---

## Test cases

```python
t = int(input())

for _ in range(t):
    ...
```

---

## Print list

```python
print(*arr)
```

---

## Read digits

```python
digits = list(map(int, input()))
```

---

# Step 15 : Converting a LeetCode solution to an OA solution

Suppose your LeetCode function is:

```python
def maxProfit(prices):
    minimum = prices[0]
    profit = 0

    for price in prices:
        minimum = min(minimum, price)
        profit = max(profit, price - minimum)

    return profit
```

In an OA, you wrap it with input/output handling:

```python
def maxProfit(prices):
    minimum = prices[0]
    profit = 0

    for price in prices:
        minimum = min(minimum, price)
        profit = max(profit, price - minimum)

    return profit


n = int(input())
prices = list(map(int, input().split()))

print(maxProfit(prices))
```

Notice that **the algorithm usually stays exactly the same**. You just add the code to read inputs and print the result.

## How to become fluent

Since you're aiming for placements and already solving LeetCode in Python, I recommend spending a few days specifically on I/O. Practice these in order:

1. Single values and multiple integers on one line.
2. Arrays and strings.
3. Multiple test cases (`t` loops).
4. Matrices.
5. Mixed inputs (e.g., `n`, then an array, then a string).
6. Fast I/O with `sys.stdin.readline`.

After about **20–30 small practice problems**, writing input/output code becomes almost automatic, and you'll be able to focus entirely on the algorithm during online assessments.
