# 33. Search in Rotated Sorted Array

"""
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = low + (high-low)//2
            
            if nums[mid]==target:
                return mid
            
            # if left half is sorted and element present
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            
            # if right half is sorted and element present
            elif nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1

