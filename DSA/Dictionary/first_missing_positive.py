# 41. First Missing Positive

class Solution1:
    def firstMissingPositive(self, nums: List[int]) -> int:
        my_map = {}
        for indx,num in enumerate(nums):
            my_map[num] = indx # no problem with repreating element
        
        for i in range(1,len(nums)+1):
            if my_map.get(i,-1) == -1:
                # found smallest positive
                return i
        return len(nums)+1
    

class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            # Before swapping, check whether the destination already contains the same value.
            while 1<=nums[i]<=len(nums) and nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                temp = nums[i]
                nums[i],nums[temp-1] = nums[temp-1],nums[i]
            i += 1
        
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1