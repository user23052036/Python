# 217. Contains Duplicate

"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
    
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    
class Solution4:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dick = {}
        for indx,num in enumerate(nums):
            if my_dick.get(num,-1)!= -1:
                return True
            my_dick[num] = indx
        return False