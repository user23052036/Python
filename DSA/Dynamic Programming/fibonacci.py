# 509. Fibonacci Number



class Solution:
    # Best is to use Binet's Formula
    # TC -> O(n)
    # SC -> O(n) + O(n)

    def fib(self, n: int) -> int:
        # dp = [-1] * (n + 1)
        # return self.top_down(dp, n)

        # return self.bottom_up(n)

        return self.space_optimization(n)

    def top_down(self, dp, n):
        if n == 0 or n == 1:
            return n

        if dp[n] != -1:
            return dp[n]

        dp[n] = self.top_down(dp, n-1) + self.top_down(dp, n-2)
        return dp[n]

    def bottom_up(self, n):
        if n == 0:
            return 0

        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    def space_optimization(self, n):
        if n <= 1:
            return n

        prev2,prev1 = 0,1
        for _ in range(2,n+1):
            prev2, prev1 = prev1, prev1+prev2

        return prev1