# object types/ data types
# Number: 123, 12.3, 3+4j, 0b111, Decimal()
# String: 'spam', "bobs'assd'"
# List: [1, [2,"chai"], 3.12] list(range(10))
# Tupil: (1,'hii','gh')
# Dictionary: {'food':'spam', 'veg':'100rs'}
# Set: set('abc'), {'a','b','c'}
# File: open('egg.txt') 
# Boolean: True, False
# Node: Node
# Function, modules, and classes

# | Type / Example         | Mutable  | Hashable  | Indexable  | Ordered  |
# | -----------------------| -------  | --------  | ---------  | -------  |
# | int (`123`)            | ❌       | ✅        | ❌         | ❌       |
# | float (`12.3`)         | ❌       | ✅        | ❌         | ❌       |
# | complex (`3+4j`)       | ❌       | ✅        | ❌         | ❌       |
# | binary int (`0b111`)   | ❌       | ✅        | ❌         | ❌       |
# | Decimal (`Decimal()`)  | ❌       | ✅        | ❌         | ❌       |
# | str (`'spam'`)         | ❌       | ✅        | ✅         | ✅       |
# | list (`[1,2]`)         | ✅       | ❌        | ✅         | ✅       |
# | tuple (`(1,2)`)        | ❌       | ✅*       | ✅         | ✅       |
# | dict (`{'a':1}`)       | ✅       | ❌        | ❌**       | ✅       |
# | set (`{'a','b'}`)      | ✅       | ❌        | ❌         | ❌       |
# | file object (`open()`) | ✅       | ❌        | ❌         | ❌       |
# | bool (`True`)          | ❌       | ✅        | ❌         | ❌       |

"""

1. Tuple is conditionally hashable
(1,2,3) → ✅ hashable
(1,[2,3]) → ❌ not hashable
Because hashability depends on all elements being hashable.

2. Dictionary is not indexable
d[0] ❌
d['key'] ✅
So it's key-accessible, not indexable in sequence sense.

3. Set is unordered
A set is an unordered collection of unique elements, meaning the items do not have a defined order, and they may appear in a 
different order every time you use them.

"""

# Advance: Decorator, Generator, Iterator, metaProgramming
number = 10
print(dir(number)) # gives possible methods associated to an object
