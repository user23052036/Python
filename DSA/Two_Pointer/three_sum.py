class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        size = len(nums)
        nums.sort(key=None, reverse=False) # N*log(N)
        result = []

        for i in range(size-2): # O(N) if we change the value of i inside loop it doesnot mattern as value is 
            # allways overwritten here
            # we will fix the outer pointer to run 2-pointer insider
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            left = i+1
            right = size-1
            target = -nums[i]  # because nums[i]+nums[left]+nums[right] = 0

            while(left<right): # O(N)
                sum = nums[left]+nums[right]

                if sum == target:
                    # found one unique solution
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    # skipping the same value to avoid duplicate
                    while(left<right and nums[left] == nums[left-1]):
                        left += 1
                    while(left<right and nums[right] == nums[right+1]): 
                        right -= 1
                
                elif sum > target:
                    right -= 1
                else:
                    left += 1
        return result
                    
                    