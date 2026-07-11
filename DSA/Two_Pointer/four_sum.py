# 18. 4Sum

"""
Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]: # type: ignore
        nums.sort(keys=None, reverse=None)
        result = []

        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:      # skipping duplicate
                continue
            for j in range(i+1,len(nums)-2):    # exactly 3-sum problem
                if j>0 and nums[j]==nums[j-1]:  # skipping duplicate
                    continue

                left = j+1
                right = len(nums)-1

                while left<right:
                    curr_sum = nums[i]+nums[j]+nums[left]+nums[right]

                    if curr_sum == target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1

                        # remove duplicates of both left and right here
                        while left<right and nums[left]==nums[left-1]:
                            left += 1
                        while left<right and nums[right]==nums[right+1]:
                            right -= 1

                    elif curr_sum<target:
                        left += 1
                    else:
                        right -= 1
        return result
