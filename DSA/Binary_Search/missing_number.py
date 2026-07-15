# 268. Missing Number

"""
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number 
in the range since it does not appear in nums.

Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number 
in the range since it does not appear in nums.

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.
"""

 # NOTE:
# Avoid writing swaps like:
# nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
#
# In Python, multiple assignment evaluates the LEFT-HAND SIDE targets
# from left to right. After nums[i] is assigned, its value changes before
# nums[nums[i]] is evaluated, so the second index may become different.
#
# Example:
# nums = [3, 0, 1], i = 1
#
# RHS is evaluated first:
# nums[nums[i]] = nums[0] = 3
# nums[i] = 0
#
# Assignment:
# nums[1] = 3        -> nums becomes [3, 3, 1]
# nums[nums[1]] = 0  -> nums[3] = 0 (IndexError)
#
# Always store the target index before swapping:
# correct = nums[i]
# nums[i], nums[correct] = nums[correct], nums[i]

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = len(nums)

        i=0
        while i<len(nums):
            if i != nums[i] and nums[i] != answer:
                indx = nums[i]
                nums[i],nums[indx] = nums[indx],nums[i]
                i -= 1
            i+= 1
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return answer
    

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i, x in enumerate(nums):
            ans = ans ^i^x
        return ans
# this is my most simplest and elegent solution we perform xor with all the index and all the array values
# if any number appears two times it gets cancelled and remaining 1 number is printed as output as it is repeated
# once

# 0 xor any_num = any_num
# same_num xor same_num = 0
# xor order does not matter