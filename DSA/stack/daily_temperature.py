# 739. Daily Temperatures

"""
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

from collections import deque
from typing import List

class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        ans = [0]*len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]-i
            stack.append(i)
        return ans


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        solution = deque()
        for indx in range(len(temperatures)-1,-1,-1):
            num = temperatures[indx]
            while stack and num>=temperatures[stack[-1]]:
                stack.pop()
            if stack:
                solution.appendleft(stack[-1]-indx)
            else:
                solution.appendleft(0)
            stack.append(indx)
        return list(solution)
