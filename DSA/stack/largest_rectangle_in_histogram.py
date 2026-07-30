# 84. Largest Rectangle in Histogram

"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.
"""

#TLE
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0

        for i in range(n):
            left = i
            while left > 0 and heights[left-1] >= heights[i]:
                left -= 1

            right = i
            while right < n-1 and heights[right+1] >= heights[i]:
                right += 1

            width = right-left+1
            ans = max(ans, heights[i]*width)

        return ans