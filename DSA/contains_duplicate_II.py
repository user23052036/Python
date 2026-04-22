
from typing import List

# brute force way
# TC -> O(N^2)
# SC -> O(1)
class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1,length):
                if abs(i-j) <= k:
                    if nums[i]==nums[j]:
                        return True
                else:
                    break
        return False

# sliding window
# TC -> O(N)
# SC -> O min(N,K)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        window = set()

        for r in range(len(nums)):
            if r-l > k:
                window.remove(nums[l])
                l += 1
            
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False