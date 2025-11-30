
# ------------------------------------------------------------- 
#
# Section 5: Sets (set)
# 
# A set is: Unordered,Unindexed,Mutable,Contains only unique items
# sets doesn't allow indexing
# -------------------------------------------------------------

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
print('Difference a - b:', a-b)


# convert a list to a set
list_5 = [4,5,6,7,8]
x = set(list_5)
print(x)



