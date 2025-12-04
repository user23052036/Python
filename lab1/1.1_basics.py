#basic- commands
#indexing in python is 0based and -1 represents last char

# Python slicing
# [i:] -> extracting ith charecter to the last charecter
# [:i] -> extracting from 0th charecter to the (i-1) charecter
# [i:j:k] -> is called python slicing


superhero = "iron man"
type(superhero)

#----------------------------------------

string = input("Enter your string: ")
print("sub_string from 4th charecter: ",string[4:])
print("sub_string upto and excluding 4th charecter: ",string[:4])
print("sliced forward string: ",string[5:10:4])
print("sliced backward string: ",string[10:5:-1])


#reverse the string
rev = string[::-1]
print(rev)

# Python slicing: [start : end : step]
# -----------------------------------------------------------
# 1) Direction is controlled ONLY by 'step'
#    - step > 0  → move forward
#    - step < 0  → move backward
#
# 2) 'start' and 'end' just define the boundary window.
#    They DO NOT control direction.
#
# 3) Example: s[::-1]
#    - start empty → Python starts from end by default
#    - end empty   → goes until beginning
#    - step = -1   → move backward one character at a time
#    => Reverses the string
#
# 4) Example: s[4:10:2]
#    - step = +2   → move forward
#    - start = 4   → begin at index 4
#    - end = 10    → stop before index 10
#    Even if end > len(s), Python silently stops at the end of string.
#
# 5) Rule of thumb:
#    - Positive step  → Python walks left-to-right
#    - Negative step  → Python walks right-to-left
#    Boundaries only limit how far it can walk.
#
# 6) Empty start/end:
#    - start empty + step>0 → begin at index 0
#    - start empty + step<0 → begin at last index
#    - end empty   → go until natural boundary in that direction


#--------------------------------------------

greeting = "hello Souvik"
print("1. ",greeting)
print("2. ",len(greeting))
print("3. ",greeting[0])
print("4. ",greeting[-1]) #printing the last indx val

greeting = greeting.replace("Souvik","Souvik Mandal")
print("5. ",greeting)

string1 = "hello"
string2 = "world"
print("1. ",string1,string2)

cost = float(35.43)
print("Bar tab = $",cost)



"""
""" """ → Multi-line String

Creates a string literal, not a comment.
Python may store it in memory unless unused.

Often used as:
Docstrings for functions, classes, modules
→ Python uses this for documentation (help(), IDE hints).
Multi-line text blocks.


| Feature                  | `#`       | `""" """`                                                       |
| ------------------------ | --------- | --------------------------------------------------------------- |
| Treated as comment?      | YES       | NO                                                              |
| Creates a string?        | NO        | YES                                                             |
| Used for docstrings?     | NO        | YES                                                             |
| Good for multiple lines? | Not ideal | YES                                                             |
| Affects memory?          | No        | Slightly (creates a string literal)                             |
| Visible in `help()`?     | No        | Yes (only when used as first line inside function/class/module) |

"""