# 153. Find Minimum in Rotated Sorted Array

"""
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted ---> click bs
        low = 0
        high = len(nums)-1
        mini = float('inf')

        while low<=high: # why equal well think of array having only one element
            mid = low + (high-low)//2

            # if duplicates found
            if nums[low]==nums[mid]==nums[high]:
                mini = min(mini,nums[low])
                low += 1
                high -= 1

            # if the whole array is sorted
            elif nums[low]<=nums[high]:
                mini = min(mini,nums[low])
                break
            
            # if left side is sorted
            elif nums[low]<=nums[mid]:
                mini = min(mini,nums[low])
                low = mid+1
            
            # right side is sorted
            elif nums[mid]<=nums[high]:
                mini = min(mini,nums[mid])
                high = mid-1
        return mini
