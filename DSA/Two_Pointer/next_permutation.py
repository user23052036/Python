# 31. Next Permutation

"""
Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [2,1,5,4,3,0,0]
Output: [2,3,0,0,1,4,5]
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_rest(i,j):
            # reverse the remaining portion
            while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1

        dip = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                dip = i-1
                break
        
        if dip == -1:
            reverse_rest(0,len(nums)-1)
        else:
            reverse_rest(dip+1,len(nums)-1)
            for i in range(dip+1,len(nums)):
                if nums[i] > nums[dip]:
                    nums[dip],nums[i] = nums[i],nums[dip]
                    break
    
        
        