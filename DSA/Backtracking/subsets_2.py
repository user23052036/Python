# 90. Subsets II

"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""


class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(index):
            # Base Case
            if index == len(nums):
                unique_subsets.add(tuple(path))
                return

            # Pick the current element
            path.append(nums[index])
            dfs(index + 1)
            path.pop()

            # Do not pick the current element
            dfs(index + 1)

        nums.sort()              # Optional but keeps duplicate subsets identical
        unique_subsets = set()
        path = []

        dfs(0)

        # Convert tuples back to lists
        ans = []
        for subset in unique_subsets:
            ans.append(list(subset))

        return ans


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def find_subset(indx,length):
            ans.append(path.copy())
            # if indx==length:
            #     return
            
            for i in range(indx,length):
                if i>indx and nums[i]==nums[i-1]:   # remove duplicate subsets
                    continue
                
                # pick current element into path
                path.append(nums[i])
                find_subset(i+1,length)
                
                # remove the inserted element
                path.pop()
        
        ans = []
        path = []
        nums.sort()
        find_subset(0,len(nums))
        return ans


# IMPORTANT: Why do we use `i > start` and NOT `i > 0` ?
#
# Duplicate elements should only be skipped if they appear as SIBLINGS
# in the SAME recursion level.
#
# Example: nums = [1,2,2]
#
# Level 0:
#             []
#           / | \
#          1  2  2   <- These two '2's are siblings.
#                           Choosing either produces the same subsets.
#                           So SKIP the second one.
#
# Level 1 after choosing [1]:
#            [1]
#           /   \
#          2     2   <- Again siblings.
#                       Skip the second one.
#
# Level 2 after choosing [1,2]:
#            [1,2]
#               |
#               2   <- NOT a sibling!
#                      This is a CHILD (a deeper recursion level).
#                      We NEED this to generate [1,2,2].
#
# Therefore:
#
# if i > start and nums[i] == nums[i-1]:
#     continue
#
# `i > start` means:
# "Skip duplicates ONLY if they are the second (or later) choice
# in the CURRENT for-loop (current recursion level)."
#
# NEVER write `i > 0`.
# `i > 0` compares against the entire array and wrongly skips duplicates
# even in deeper recursion levels, causing valid subsets like [1,2,2]
# to disappear.