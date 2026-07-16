# 238. Product of Array Except Self

"""
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_pro = [0]*len(nums)
        suffix_pro = [0]*len(nums)

        res = [0]*len(nums)
        prefix_pro[0] = 1
        for i in range(1,len(nums)):
            prefix_pro[i] = prefix_pro[i-1]*nums[i-1]
            if prefix_pro[i]==0:
                break # as rest product will also be 0
        
        suffix_pro[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            suffix_pro[i] = suffix_pro[i+1]*nums[i+1]
            if suffix_pro[i]==0:
                break
        
        for i in range(len(res)):
            res[i] = prefix_pro[i]*suffix_pro[i]
        return res


    # optimized for space complexity
    class Solution2:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            length = len(nums)
            prefix = 1
            suffix = 1
            result = [1]*length
            for i in range(len(nums)):
                if i!=0:
                    prefix *= nums[i-1]
                    suffix *= nums[length-i]
                
                result[i] *= prefix
                result[length-i-1] *= suffix
            return result    