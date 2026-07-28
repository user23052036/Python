# 17. Letter Combinations of a Phone Number

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that 
the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 
1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_map = {}
        curr = ord('a')
        for digit in range(2, 10):
            letters = ""
            # 7 and 9 have 4 letters
            count = 4 if digit in (7,9) else 3
            for _ in range(count):
                letters += chr(curr)
                curr += 1
            my_map[str(digit)] = letters

        def backtrack(indx):
            if indx==len(digits):
                ans.append("".join(word))
                return
            
            for i in range(len(my_map[digits[indx]])):

                word.append(my_map[digits[indx]][i])
                backtrack(indx+1)
                word.pop()
        
        ans = []
        word = []
        backtrack(0)
        return ans
    
# ---------------- Mistake I made ----------------
# I initially wrote:
#     if indx == len(my_map[digits[indx]])
#
# This was wrong because `indx` represents the current DIGIT being processed,
# not the position inside the letters mapped to that digit.
#
# Correct base case:
#     if indx == len(digits)
#
# When indx == len(digits), it means I've chosen one letter for every digit,
# so the current combination is complete.
# -----------------------------------------------



# ---------------- Mistake I made ----------------
# I initially called:
#     backtrack(i + 1)
#
# Here `i` is the index of the chosen LETTER inside "abc"/"def", etc.
# It has nothing to do with which digit I'm processing.
#
# The recursion should always move to the NEXT DIGIT:
#     backtrack(indx + 1)
#
# Mental model:
# indx -> current digit (2,3,4,...)
# i    -> current letter within that digit (a,b,c)
# Never mix these two indices.
# -----------------------------------------------



# ---------------- Lesson learned ----------------
# In backtracking, always ask:
#
# 1. What does my recursive parameter represent?
#    -> Here: the current digit index.
#
# 2. What does my loop variable represent?
#    -> Here: the current letter choice for that digit.
#
# If these represent different things, they should NEVER be used
# interchangeably.
# -----------------------------------------------