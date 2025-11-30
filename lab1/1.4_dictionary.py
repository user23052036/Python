# -------------------------------------------------------------
#
# Section 1: Dictionaries (dict)
#
# A dictionary stores key → value pairs.
# Keys must be unique & immutable (string, number, tuple).
# Values can be any type.
# Lookup is O(1) average → very fast.
#
# -------------------------------------------------------------

"""

The isinstance() Function in Python is a built-in function to check if an object is an example of a 
class or type, or any of its subclasses. 

isinstance(object, classinfo) True/False

"""

# the below dictionary has 4 element each element has a key,value pair
# dictionary don't allow duplicate elements

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
print("Chicken:", prices.get('Chicken', 'Not Available')) # unsafe way prices["chicken"]


"""
Why list() is used with keys(), values(), items():

These methods return "view objects" (dict_keys, dict_values, dict_items).
They cannot be indexed directly. Example:

k = prices.keys()
k[0]   # ❌ ERROR: dict_keys is not subscriptable

To use indexing, convert the view into a normal list:

k = list(prices.keys())
k[0]   # ✔ Works

Same for values() and items():
list(prices.values())[1]
list(prices.items())[0]

So list() is used only to ENABLE indexing and make the output look like a normal list.
"""


# Keys / values / items
print('\nKeys:', list(prices.keys()))
print('Values:', list(prices.values()))
print('Items:', list(prices.items()))


# Iteration over dict
print('\nIterate keys and values:')
for k,v in prices.items():
    print(k, '->', v)


# Deleting keys
del prices['Beer']
print('\nAfter delete Beer:', prices)

# Check existence
print('\nIs Bacon in prices?','Bacon' in prices) # True/False




