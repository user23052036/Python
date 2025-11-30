"""
python_cheatsheet.py
"""

# -------------------------------------------------------------
# Section 1: Dictionaries (dict)

#A dictionary stores key → value pairs.
#Keys must be unique & immutable (string, number, tuple).
#Values can be any type.
#Lookup is O(1) average → very fast.
# -------------------------------------------------------------

prices = {
    "Eggs": 2.50,
    "Steak": 14.60,
    "Bacon": 5.30,
    "Beer": 14.05,
}

print('1: ', prices)
print('2: ', type(prices))
print('Price of Bacon:', prices['Bacon']) 

# Add / modify / delete
prices["Milk"] = 3.00        # add
prices['Eggs'] = 2.90        # update

print('\nAfter add/update:')
print(prices)

# Safe access using get -> avoids KeyError, can provide default
print("Chicken:", prices.get('Chicken', 'Not Available'))

# Keys / values / items
print('\nKeys:', list(prices.keys()))
print('Values:', list(prices.values()))
print('Items:', list(prices.items()))

# Iteration over dict
print('\nIterate keys and values:')
for k, v in prices.items():
    print(k, '->', v)

# Deleting keys
del prices['Beer']
print('\nAfter delete Beer:', prices)

# Check existence
print('\nIs Bacon in prices?', 'Bacon' in prices)



# -------------------------------------------------------------
# Section 2: Tuples (tuple)
# -------------------------------------------------------------
sep('Tuples (tuple)')

t1 = (6, 7)
t2 = (33, 12)
print('t1:', t1, 't2:', t2)
print('Indexing t1[0]:', t1[0])
print('Concat t1 + t2:', t1 + t2)
print('Length:', len(t1))

# Single element tuple
single = (5,)    # comma is required
not_tuple = (5)  # int
print('single is tuple?', isinstance(single, tuple))
print('not_tuple is tuple?', isinstance(not_tuple, tuple))

# Unpacking
a, b = t1
print('Unpacked a,b =', a, b)

# -------------------------------------------------------------
# Section 3: Lists (list)
# -------------------------------------------------------------
sep('Lists (list)')

arbitory_lst = [3, 66, 45, 2.213, True, 'true', 'Midori']
print('arbitory_lst:', arbitory_lst)

numbers = [4, 6, 7, 5, type(arbitory_lst), arbitory_lst]
print('\nnumbers initial:')
pprint(numbers)

# Common mutations
numbers.insert(2, 'surprise')   # insert at index 2
numbers.append(89)               # append to end
numbers.remove(6)                # remove first occurrence of 6

# IMPORTANT: numbers[-2] is the second-last element
print('\nnumbers after mutations:')
pprint(numbers)
print('\nShowing numbers[-2] (second last):', numbers[-2])

# Because numbers[-2] references arbitory_lst, mutate that nested list:
if isinstance(numbers[-2], list):
    numbers[-2].remove(66)  # remove 66 from the nested list

print('\nAfter removing 66 from nested list:')
pprint(numbers)

# Indexing and negative indexing
lst = [10, 20, 30, 40]
print('\nlst[0]=', lst[0], 'lst[-1]=', lst[-1])

# Slicing (non-destructive)
print('\nlst[1:3] ->', lst[1:3])
print('lst[:2] ->', lst[:2])
print('lst[2:] ->', lst[2:])

# List comprehension
squares = [x*x for x in range(5)]
print('\nList comprehension squares:', squares)

# Nested lists (matrix)
mat = [[1, 2], [3, 4]]
print('\nmat[1][0] =', mat[1][0])

# Copying lists: reference vs shallow copy vs deep copy
a = [1, 2, [10, 20]]
b = a           # reference (both names point to same list)
c = a[:]        # shallow copy (outer list new, inner references same)
d = copy.deepcopy(a)  # deep copy (fully independent)

print('\nOriginal a:', a)
print('b (reference) before mutate:', b)

# Mutate inner list
a[2].append(99)
print('\nAfter a[2].append(99):')
print('a:', a)
print('b (reflects change):', b)
print('c (shallow copy) reflects inner change:', c)
print('d (deepcopy) unaffected:', d)

# Useful list methods (demonstration)
methods_demo = [3, 1, 4]
methods_demo.append(2)
methods_demo.insert(1, 9)
print('\nmethods_demo after append/insert:', methods_demo)
methods_demo.sort()
print('sorted:', methods_demo)
methods_demo.pop()  # removes last
print('pop:', methods_demo)

# -------------------------------------------------------------
# Section 4: String slicing & reversing (very common traps)
# -------------------------------------------------------------
sep('String slicing & reversing')

s = 'abcdefghijklmnopqrstuvwxyz'
print('string s =', s)

# General form: s[start:end:step]
print('s[4:10:2] ->', s[4:10:2])  # start at index4 (e), stop before 10 (j), step 2 -> e g i

# Reverse a string
rev = s[::-1]
print('\nReverse s[::-1] ->', rev)

# Explanation for tricky slices:
# - If step > 0: start defaults to 0, end defaults to len(s)
# - If step < 0: start defaults to len(s)-1, end defaults to -1 (stop before -1)
# Examples:
print('s[5::-1] ->', s[5::-1])   # start index5 ('f'), go backwards to start -> 'fedcba'
print('s[5::1]  ->', s[5::1])    # start index5, go forward to end -> substring from 'f' onward

# More slicing boundary examples
print('\nEmpty slice (start >= end with positive step):', s[10:5:1])
print('Negative step empty slice (start <= end with negative step):', s[1:5:-1])

# Common idiom: skip characters
print('Every 3rd char:', s[::3])

# -------------------------------------------------------------
# Section 5: Sets (set)
# -------------------------------------------------------------
sep('Set (set)')

st = {1, 2, 3, 3}
print('st (duplicates removed):', st)
st.add(5)
print('after add(5):', st)
st.discard(9)  # no error if not present
print('after discard(9):', st)

a = {1, 2, 3}
b = {3, 4, 5}
print('\nUnion:', a | b)
print('Intersection:', a & b)
print('Difference a - b:', a - b)

# -------------------------------------------------------------
# Section 6: Mutability, identity, and equality
# -------------------------------------------------------------
sep('Mutability, identity, equality')

x = [1, 2]
y = [1, 2]
print('x == y ->', x == y)    # True (value equality)
print('x is y ->', x is y)    # False (different objects)

z = x
print('z is x ->', z is x)    # True (same object)

# -------------------------------------------------------------
# Section 7: Useful built-ins and patterns
# -------------------------------------------------------------
sep('Built-ins & patterns')

print('len(list):', len([1,2,3]))
print('sum([1,2,3]):', sum([1,2,3]))
print('sorted([3,1,2]):', sorted([3,1,2]))

# enumerate & zip
letters = ['a', 'b', 'c']
for idx, ch in enumerate(letters, start=1):
    print('enumerate:', idx, ch)

nums = [10, 20, 30]
for a, b in zip(letters, nums):
    print('zip pair:', a, b)

# swap variables (pythonic)
a, b = 5, 10
a, b = b, a
print('\nSwap a,b ->', a, b)

# Ternary expression
n = 5
parity = 'odd' if n % 2 else 'even'
print('n parity:', parity)

# -------------------------------------------------------------
# Section 8: Common pitfalls & tips
# -------------------------------------------------------------
sep('Common pitfalls & tips')

# 1. Don't use mutable default args in functions
print('Mutable default arg example (avoid):')

def bad_append(value, lst=[]):
    lst.append(value)
    return lst

print('call1:', bad_append(1))
print('call2:', bad_append(2))  # shares same list -> surprising

# Correct approach
print('\nCorrect approach using None:')
def good_append(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print('call1:', good_append(1))
print('call2:', good_append(2))  # independent lists

# 2. When iterating and removing elements from a list, iterate over a copy
print('\nIterate over copy when removing:')
items = [1,2,3,4]
for x in items[:]:
    if x % 2 == 0:
        items.remove(x)
print('after removing evens:', items)

# -------------------------------------------------------------
# Section 9: Quick reference examples (compact)
# -------------------------------------------------------------
sep('Quick reference examples')

# dict comprehension
dcomp = {x: x*x for x in range(5)}
print('dict comprehension:', dcomp)

# set comprehension
scomp = {x%2 for x in range(6)}
print('set comprehension:', scomp)

# generator expression (lazy)
g = (x*x for x in range(5))
print('generator next():', next(g))

# try/except example for KeyError
print('\ntry/except KeyError:')
try:
    print(prices['NonExistent'])
except KeyError:
    print('Key not found, used exception handling')

# isinstance checks
print('\nisinstance([1,2], list):', isinstance([1,2], list))

# -------------------------------------------------------------
# Section 10: Functions demonstrating useful idioms
# -------------------------------------------------------------
sep('Helper functions')

def reverse_string(s: str) -> str:
    """Return reversed string using slicing."""
    return s[::-1]

print("reverse_string('hello') ->", reverse_string('hello'))


def chunk_list(lst, chunk_size):
    """Yield successive chunk_size-sized chunks from lst."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i+chunk_size]

print('\nChunks of [1..9] with size 3:')
for c in chunk_list(list(range(1,10)), 3):
    print(c)

# -------------------------------------------------------------
# End: try running as script
# -------------------------------------------------------------
if __name__ == '__main__':
    print('\n\nDone — run the file and tweak examples as you learn.')
