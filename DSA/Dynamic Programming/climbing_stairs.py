# 70. Climbing Stairs

"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        def recursion(indx):
            nonlocal count

            if indx>n:
                return
            if indx == n:
                count += 1
                return
            
            recursion(indx+1)
            recursion(indx+2)


        def dynamic_p(indx):
            if indx<0:
                return 0
            if indx == 0:
                return 1
            if dp[indx] != -1:
                return dp[indx]

            dp[indx] = dynamic_p(indx-1) + dynamic_p(indx-2)
            return dp[indx]
        

        def tabulation():
            dp[0] = 1
            dp[1] = 1

            for i in range(2,n+1):
                dp[i] = dp[i-1]+dp[i-2]
            return dp[n]


        def space_optimization():
            if n<=1:
                return 1

            prev = 1
            prev2 = 1
            curr = 0
            for i in range(2,n+1):
                curr = prev + prev2
                prev2 = prev
                prev = curr
                
            return curr


        count = 0
        dp = [-1]*(n+1)
        return space_optimization()
        