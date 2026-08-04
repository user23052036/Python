# 213. House Robber II
# SAME Q WITH CIRCULAR ARRAY

# TLE
class Solution:
    def rob(self, nums: List[int]) -> int:
        def memoization(lb, indx):
            if indx==lb:
                return nums[indx]
            if indx<lb:
                return 0
            
            if dp[indx] != -1:
                return dp[indx]
            
            pick = nums[indx] + memoization(lb, indx-2)
            notpick = 0 + memoization(lb, indx-1)

            return max(pick,notpick)
        
        n = len(nums)
        if n==1:
            return nums[0]
            
        dp = [-1]*n
        ans1 = memoization(0,n-2)
        ans2 = memoization(1,n-1)

        return max(ans1,ans2)


# space optimization
# bottom -> up
class Solution:
    def rob(self, nums: List[int]) -> int:
        def space_opti(lb, ub):
            prev2 = 0
            prev = nums[lb]

            for i in range(lb+1,ub+1):
                take = nums[i]
                if i-1>0:
                    take += prev2
                
                nottake = prev
                
                curr = max(take, nottake)
                prev2 = prev
                prev = curr
            return prev
        
        n = len(nums)
        if n==1:
            return nums[0]

        ans1 = space_opti(0,n-2)
        ans2 = space_opti(1,n-1)

        return max(ans1,ans2)