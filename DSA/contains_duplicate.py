from typing import List

# Brute force way
# TC -> O(N*log(N))
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
    

# TC -> O(N)
# SC -> O(N)
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    

# TC -> O(N)
# SC -> O(N)
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)