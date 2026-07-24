# 78. Subsets

"""
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
"""

# O(2^n *n) TC as there are 2^n subsets and to print we assume avg size to be n/2 --> n so n*2^n
# stack space is O(n)
class Solution1:
    def search_dfs(self,nums,i,n,stack,ans):
        if i>=n:
            ans.append(stack.copy())
            return
    
        # pick case
        stack.append(nums[i])
        self.search_dfs(nums,i+1,n,stack,ans)
        stack.pop()

        # not pick case
        self.search_dfs(nums,i+1,n,stack,ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        ans = []
        
        self.search_dfs(nums,0,len(nums),stack,ans)
        return ans


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(indx,length):
            ans.append(stack.copy())
            # if indx==length:
            #     return

            for i in range(indx,length):
                # adds to the path and move to next indx rec call
                stack.append(nums[i])
                backtrack(i+1,length)
                stack.pop()
        ans = []
        stack = []
        backtrack(0,len(nums))
        return ans


# -----------------------------------------------------------------------------------------
# IMPORTANT:
#
# In the for-loop style backtracking, we do NOT need:
#
#     if start == len(nums):
#         return
#
# because the loop itself becomes the base case.
#
# When start == len(nums):
#
#     for i in range(len(nums), len(nums)):
#
# executes zero iterations, so the function naturally reaches its end
# and returns.
#
# Think of it as:
#
#     "No candidates left to choose."
#
# rather than
#
#     "Reached the base case."
#
# This optimization ONLY works for the for-loop recursion pattern.
#
# It does NOT work in Pick/Not Pick recursion because that approach
# directly accesses nums[index]. Without an explicit base case,
# it would try to access nums[len(nums)] and crash with IndexError.

# -----------------------------------------------------------------------------------------------



# IMPORTANT: Use stack.copy() instead of stack.
#
# 'stack' is a single list object that is reused throughout the recursion.
# We keep modifying it using append() and pop() during backtracking.
#
# Example:
# nums = [1, 2]
#
# Current recursion states:
#
# stack = []
# ans.append(stack)      # ans = [[]]
#
# stack.append(1)
# ans.append(stack)      # ans = [[1], [1]]
#
# stack.append(2)
# ans.append(stack)      # ans = [[1,2], [1,2], [1,2]]
#
# stack.pop()
# stack.pop()
#
# Final stack = []
#
# Since every element in 'ans' is pointing to the SAME list object,
# after backtracking all entries become:
#
# ans = [[], [], []]
#
# To preserve the current state of the stack at each leaf node,
# we store a COPY of the list instead of its reference.
#
# Using stack.copy():
#
# stack = []      -> ans = [[]]
# stack = [1]     -> ans = [[], [1]]
# stack = [1,2]   -> ans = [[], [1], [1,2]]
#
# These are separate list objects, so later modifications to 'stack'
# do not affect the previously stored subsets.
# ans.append(stack.copy())