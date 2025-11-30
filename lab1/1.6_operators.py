"""
Operators in Python:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators

"""


num_1 = 20
num_2 = 10

# addition
sum = num_1 + num_2
print('sum = ',sum)

# subtraction
diff = num_1 - num_2
print('difference = ',diff)

# multiplication
pro = num_1 * num_2
print('product = ',pro)

# division
quo = num_1 / num_2
print('quotient = ',quo)

# exponent
exp = num_1**num_2   # 20^10
print('exponent = ',exp)

# modulus
mod = num_1 % num_2
print('reminder = ',mod)

#-------------------------------------------------------------
a = 10

print( a>20 and a>5)
print( a>20 or a>5)
print( not( a>8 and a>5))
#--------------------------------------------------------------

# == checks VALUE equality logical operator.
# is checks OBJECT identity (same memory location) identity operator.

x = 5
y = 5
print(x is y) # True (same cached object)
print(x is not y)

# Two lists with same value
a = [10, 20]
b = [10, 20]

print(a == b)  # True  (values same)
print(a is b)  # False (different objects)

# Assigning
c = a
print(a is c)  # True  (same object)

# Numbers (sometimes cached)
x = 1000
y = 1000
print(x == y)  # True
print(x is y)  # Usually False (but depends on Python)


#--------------------------------------------------------------
 # Membership operator

a = 5
b =10

c = [1,2,3,4,5]
print( a in c)
print( b in c)

#-------------------------------------------------------------
