# 198. House Robber

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money 
stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems 
connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money 
you can rob tonight without alerting the police.


Input: nums = [1,2,3,1]
Output: 4

Input: nums = [2,7,9,3,1]
Output: 12
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        def memoization(indx):
            if indx==0:
                return nums[indx]
            if indx<0:
                return 0
            if dp[indx] != -1:
                return dp[indx]
            
            pick = nums[indx] + memoization(indx-2)
            notpick = memoization(indx-1)

            dp[indx] = max(pick, notpick)
            return dp[indx]

        dp = [-1]*len(nums)
        return memoization(len(nums)-1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev = nums[0]

        for i in range(1,len(nums)):
            take = nums[i]
            if i-1>0:
                take += prev2
            
            nottake = prev
            
            curr = max(take, nottake)
            prev2 = prev
            prev = curr
        return prev