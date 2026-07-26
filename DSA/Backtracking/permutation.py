# 46. Permutations

class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(nums)==len(path):
                ans.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # choose the current
                used[i] = True
                path.append(nums[i])

                backtrack()

                used[i] = False
                path.pop()
        
        used = [False]*len(nums)
        path = []
        ans = []
        
        backtrack()
        return ans



class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(indx):
            if indx==len(nums):
                ans.append(nums.copy())
                return
            
            for i in range(indx,len(nums)):
                
                # choose the current
                nums[i],nums[indx] = nums[indx],nums[i]
                backtrack(indx+1)
                nums[i],nums[indx] = nums[indx],nums[i]
        ans = []
        
        backtrack(0)
        return ans




# ==========================================================
# SWAP BACKTRACKING
#
# Unlike the used[] approach, we don't ask:
#
#     "Which number should I pick next?"
#
# Instead we ask:
#
#     "Which number should occupy this POSITION?"
#
# Example:
#
# nums = [1,2,3]
#
# Position 0:
#
#     try 1
#     try 2
#     try 3
#
# by swapping each candidate into index 0.
#
# Once position 0 is fixed,
# recursively fill position 1.
#
# Once position 1 is fixed,
# recursively fill position 2.
#
# Therefore:
#
#     indx = current POSITION being filled
#
# NOT
#
#     current element chosen.
#
# That's why recursion is always:
#
#     backtrack(indx + 1)
#
# regardless of which 'i' was swapped.
#
# The array itself stores the partial permutation,
# so no extra 'path' array is needed.
# ==========================================================