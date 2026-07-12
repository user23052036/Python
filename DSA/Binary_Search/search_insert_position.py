# 35. Search Insert Position

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: # type: ignore
        # lower bound question 
        low = 0
        high = len(nums)-1
        pos = len(nums)

        while low<=high:
            mid = low + (high-low)//2

            if nums[mid]>=target:
                pos = mid
                high = mid-1
            else:
                low = mid+1
        return pos
    

# recursive solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: # type: ignore
        def lower_bound(low: int, high: int, ans: int) -> int:
            if low > high:
                return ans

            mid = low + (high-low)//2

            if nums[mid] >= target:
                return lower_bound(low,mid-1,mid)
            else:
                return lower_bound(mid+1,high,ans)

        return lower_bound(0, len(nums)-1,len(nums))
