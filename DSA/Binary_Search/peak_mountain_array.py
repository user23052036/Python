# 852. Peak Index in a Mountain Array

"""
You are given an integer mountain array arr of length n where the values increase to a peak 
element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.
"""

class Solution1:
    def peakIndexInMountainArray(self, arr: List[int]) -> int: # type: ignore
        # start and end exception case
        if arr[0]>arr[1]:
            return arr[0]
        if arr[len(arr)-1] > arr[len(arr)-2]:
            return arr[len(arr)-1]
        
        # main logic
        # 1. ascending case
        # 2. descending case
        # 3. peak case
        low = 1
        high = len(arr)-2

        while low<=high:
            mid = low + (high-low)//2

            if mid+1<len(arr) and mid-1>=0:
                if arr[mid-1]<arr[mid]>arr[mid+1]: # peak case
                    return mid
                elif arr[mid-1]<arr[mid]<arr[mid+1]: # ascending case
                    low = mid+1
                else:
                    high = mid-1   # descending case
            else:
                return -1
            
class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int: # type: ignore
        low, high = 0, len(arr) - 1
        mini = high + 1

        while low <= high:
            mid = low + (high - low) // 2

            # If the next element is smaller or equal,
            # eliminate the right half.
            if mid + 1 <= len(arr) - 1 and arr[mid] >= arr[mid + 1]:
                mini = min(mini, mid)
                high = mid - 1
            else:
                low = mid + 1

        return mini
    
# Input
arr = list(map(int, input("Enter mountain array: ").split()))

# Output
obj = Solution1()
print("Peak Index:", obj.peakIndexInMountainArray(arr))