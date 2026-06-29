# link: https://www.geeksforgeeks.org/problems/overlapping-intervals--174556/1

"""
You are given a 2D array arr[][] which represents a set of intervals, where each element arr[i] = [start, end] 
defines an interval.
Your task is to determine if any two intervals in the given set overlap.

Note: Two intervals [a, b] and [c, d] overlap if they have at least one common value, i.e., a ≤ d and c ≤ b.
"""

class Solution:
    def isIntersect(self, intervals):
        # Code Here
        intervals.sort(key = lambda x:x[0])
        write = 0
        for i in range(1, len(intervals)):
        # merge condition
            if intervals[i][0] <= intervals[write][1]:
                return True
            else:
                write += 1
                intervals[write] = intervals[i]
        return False