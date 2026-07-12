# 704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int: # type: ignore
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = low+ (high-low)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return -1
    

# recursive solution

class Solution:
    def search(self, nums: List[int], target: int) -> int: # type: ignore
        def binary_search(low: int, high: int) -> int:
            if low > high:
                return -1

            mid = low + (high - low)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid+1, high)
            else:
                return binary_search(low, mid-1)

        return binary_search(0,len(nums)-1)