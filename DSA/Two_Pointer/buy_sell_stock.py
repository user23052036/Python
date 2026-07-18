# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=0
        maxi = 0

        while sell<len(prices):
            profit = prices[sell]-prices[buy]
            if profit>maxi:
                maxi = profit
            elif profit<0:
                buy = sell
            sell += 1
        return maxi