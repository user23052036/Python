# 34. Find First and Last Position of Element in Sorted Array

"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution:
    def lower_bound(self, nums, target):
        low = 0
        high = len(nums)-1
        indx = len(nums)

        while low<=high:
            mid = low + (high-low)//2

            if nums[mid]>=target:
                indx = mid
                high = mid-1
            else:
                low = mid+1
        return indx
    
    def upper_bound(self, nums, target):
        low = 0
        high = len(nums)-1
        indx = len(nums)

        while low<=high:
            mid = low + (high-low)//2

            if nums[mid]>target:
                indx = mid
                high = mid-1
            else:
                low = mid+1
        return indx
    
    def searchRange(self, nums: List[int], target: int) -> List[int]: # type: ignore
        lb = self.lower_bound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        ub = self.upper_bound(nums,target)
        return [lb, ub-1]


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]: # type: ignore
        size = len(nums)

        # Find the leftmost occurrence
        low, high = 0, size - 1
        first = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # Find the rightmost occurrence
        low, high = 0, size - 1
        last = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]