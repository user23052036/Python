# 22. Generate Parentheses

"""
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate_string(n):
            return '('*n + ')'*n

        def valid_paranthesis(my_str:str) -> bool:
            stack = []

            for ch in my_str:
                if ch=='(':
                    stack.append(ch)
                else: # ')' case
                    if not stack:
                        return False
                    else:
                        stack.pop()
            return len(stack)==0
        
        def backtrack():
            if len(path)==len(my_str):
                if valid_paranthesis("".join(path)):
                    ans.append("".join(path.copy()))
                return 
            
            for i in range(len(my_str)):
                if i>0 and my_str[i]==my_str[i-1] and not used[i-1]:
                    continue
                
                if used[i]:
                    continue

                used[i] = True
                path.append(my_str[i])

                backtrack()

                used[i] = False
                path.pop()
        
        my_str = generate_string(n)
        path = []
        used = [False]*len(my_str)
        ans = []

        backtrack()
        return ans

                


# # ================= PERMUTATIONS II DUPLICATE RULE =================
#
# Suppose:
#
# nums = [1, 2, 2, 2]
#
# To understand the algorithm, temporarily label the duplicates:
#
# nums = [1, 2a, 2b, 2c]
#
# (These labels DO NOT exist in the actual array. They are only for
# understanding the recursion.)
#
# Think of identical elements as standing in a queue:
#
#     2a  --->  2b  --->  2c
#
# Rule:
# A duplicate is allowed to be picked ONLY AFTER the previous duplicate
# has already been picked.
#
# ---------------------------------------------------------------
# Root of recursion:
#
# used = [F, F, F, F]
#
# Trying to pick:
#
#     2a  ✔ Allowed
#
#     2b  ✘ Not allowed because 2a is still unused.
#
#     2c  ✘ Not allowed because 2b is still unused.
#
# Why?
#
# Starting with 2b or 2c produces exactly the same permutation tree
# as starting with 2a. So those branches are duplicates.
#
# ---------------------------------------------------------------
# Suppose we've already picked 2a:
#
# path = [2a]
#
# used = [F, T, F, F]
#
# Now:
#
#     2b  ✔ Allowed because 2a is already used.
#
# ---------------------------------------------------------------
# Suppose we've picked:
#
# path = [2a, 2b]
#
# used = [F, T, T, F]
#
# Now:
#
#     2c  ✔ Allowed because 2b is already used.
#
# ---------------------------------------------------------------
# Therefore the condition is:
#
# if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
#     continue
#
# Read it as:
#
# "If the previous identical element is STILL AVAILABLE,
# then I'm not allowed to pick the current duplicate."
#
# NEVER think:
#
#     "If previous duplicate is used, skip current."
#
# That's the opposite of what we want.
#
# We WANT to allow:
#
#     2a
#     2a -> 2b
#     2a -> 2b -> 2c
#
# and FORBID:
#
#     2b before 2a
#     2c before 2b
#
# ================================================================