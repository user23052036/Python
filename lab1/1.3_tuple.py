
# -------------------------------------------------------------
#
# Section 2: Tuples (tuple) c++ quivalent is pair
#
# A tuple is an ordered, immutable, indexable collection that can store multiple data types.
# can be used as dictionary keys.
# t = 1, 2, 3     # still a tuple, paranthesis is optional
#
# -------------------------------------------------------------


t1 = (6, 7,"midori",67.77)
t2 = (33, 12)

print('\nt1:', t1, 't2:', t2)
print('Indexing t1[0]:', t1[0])
print('Concat t1 + t2:', t1 + t2)
print('Length:', len(t1))

# Single element tuple
single = (5,)    # comma is required
not_tuple = (5)  # int

print('single is tuple?', isinstance(single, tuple)) #True/False
print('not_tuple is tuple?', isinstance(not_tuple, tuple)) #True/False


# converting  a list to a tuple
my_list = [3,4,5,6]
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)


# Unpacking
# a,b = t1
# print('Unpacked a,b =', a, b)



