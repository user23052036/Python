# Python syntax and data-types

#Directory
# A dictionary (key–value pairs). Keys must be unique, values can be any type.
prices={
    "Eggs":2.50,
    "Steak":14.60,
    "Bacon":5.30,
    "Beer":14.05
    }

print("1: ",prices)
print("2: ",type(prices))
print("The price of bacon is: ",prices["Bacon"])



# Tuples 
# are immutable containers where data cannot be changed once assigned
# Use tuples when you want fixed data that should never be modified

tupil1 = (6,7)
tupil2 = (33,12)

print(tupil1,tupil2)


# Lists 
# can store arbitrary values of different data types
# Lists are mutable -> you can add, remove, or change elements
# A list can even store another list or even a data type itself


arbitory_lst = [3,66,45,2.213,True,"true","Midori"]
print(arbitory_lst)

numbers = [4,6,7,5,type(arbitory_lst),arbitory_lst]
print(numbers)
numbers.insert(2,"suprise")
print(numbers)
numbers.append(89) # at the end
numbers.remove(6)
numbers[-2].remove(66)  # [[4, "suprise", 7, 5, <class 'list'>, arbitory_lst, 89]
print(numbers)

