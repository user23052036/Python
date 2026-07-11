# 977. Squares of a Sorted Array

"""
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: # type: ignore
        
        size = len(nums)
        small=0
        large=size-1
        result = [0]*size
        back = size-1

        while small<=large:
            num1 = abs(nums[small])
            num2 = abs(nums[large])

            if num1>=num2:
                result[back] = num1*num1
                small += 1
            else:
                result[back] = num2*num2
                large -= 1
            back -= 1
        return result
        