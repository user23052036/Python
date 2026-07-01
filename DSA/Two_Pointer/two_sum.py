from typing_extensions import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dick = {}

        for indx,num in enumerate(nums):
            my_dick[num] = indx

        for indx,num in enumerate(nums):
            complement_indx = my_dick.get(target - num, -1)
            
            if complement_indx != -1 and complement_indx != indx:
                return [indx, complement_indx]
            

class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dick = {}
        for i in range(len(nums)):
            curr_indx = i
            complement_val = target - nums[i]
            complement_indx = my_dick.get(complement_val,-1)
            if complement_indx != -1:
                return [curr_indx,complement_indx] 
            my_dick[nums[i]] = curr_indx


        