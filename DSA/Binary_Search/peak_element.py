# 162. Find Peak Element

"""
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, 
or index number 5 where the peak element is 6.
"""

class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums)==1:
            return 0

        # start and end exception case
        if nums[0]>nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        
        # main logic
        # 1. ascending case
        # 2. descending case
        # 3. peak case
        # 4. valley case
        low = 1
        high = len(nums)-2

        while low<=high:
            mid = low + (high-low)//2

            if mid+1<len(nums) and mid-1>=0:
                if nums[mid-1]<nums[mid]>nums[mid+1]: # peak case
                    return mid
                elif nums[mid-1]<nums[mid]<nums[mid+1]: # ascending case
                    low = mid+1
                else:
                    high = mid-1   # descending case also includes valley case
            else:
                return -1

