import copy
"""
copy() : shallow copy for the outer structure
deepcopy() : complete copy

"""


# -------------------------------------------------------------
#
# Section 3: Lists (list) like vector in cpp 
#
# A list is an ordered, mutable, dynamic collection that can store mixed data types.
# supports indexing and slicing
# 
# common list operations: 
# append()
# insert()
# pop()
# remove()
# sort()
# reverse()
# extend() 
#
# -------------------------------------------------------------

arbitory_lst = [3, 66, 45, 2.213, True, 'true', 'Midori']
print('arbitory_lst:', arbitory_lst)

numbers = [4, 6, 7, 5, type(arbitory_lst), arbitory_lst]
print('\nnumbers initial:')
print(numbers)


#joinning two lists
list1 = [1,2,34.43,5]
list2 = [7,6,5,8.3]
list3 = list1 + list2
print(list3)

# Common mutations
numbers.insert(2, 'surprise')   # insert at index 2
numbers.append(89)               # append to end
numbers.remove(6)                # remove first occurrence of 6


# IMPORTANT: numbers[-2] is the second-last element
print('\nnumbers after mutations:')
print(numbers)
print('\nShowing numbers[-2] (second last):', numbers[-2])

# Because numbers[-2] references arbitory_lst, mutate that nested list:
if isinstance(numbers[-2], list):
    numbers[-2].remove(66)  # remove 66 from the nested list

print('\nAfter removing 66 from nested list:')
print(numbers)


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

# List comprehension = short form of (for loop + append)
# Format: [expression for variable in iterable if condition]
# Example:
# nums = [x for x in range(10) if x % 2 == 0]
# Same as:
# nums = []
# for x in range(10):
#     if x % 2 == 0:
#         nums.append(x)



# Nested lists (matrix)
mat = [[1, 2], [3, 4]]
print('\nmat[1][0] =', mat[1][0])


# Copying lists: reference vs shallow copy vs deep copy
a = [1, 2, [10, 20]]
b = a           # reference (both names point to same list)
c = a[:]        # shallow copy (outer list new, inner references same) [10,20] is still referenced by c to a
# can also do c = copy.copy(a)
d = copy.deepcopy(a)  # deep copy (fully independent)

print('\nOriginal a:', a)
print('b (reference):', b)


# Mutate inner list
a[2].append(99)
print('\nAfter a[2].append(99):')
print('a:', a)
print('b reference(reflects change):', b)
print('c (shallow copy) reflects inner change:', c)
print('d (deepcopy) unaffected:', d) 
#after modification deepcopy is not changed as it is a completely seperate copy no references or inner links


# Useful list methods (demonstration)
methods_demo = [3, 1, 4]
methods_demo.append(2)
methods_demo.insert(1, 9)
print('\nmethods_demo after append/insert:', methods_demo)
methods_demo.sort()
print('sorted:', methods_demo)
methods_demo.pop()  # removes last
print('pop:', methods_demo)


# Mutability, identity, and equality
x = [1, 2]
y = [1, 2]
print('x == y ->', x == y)    # True (value equality)
print('x is y ->', x is y)    # False (different objects)

z = x
print('z is x ->', z is x)    # True (same object)




