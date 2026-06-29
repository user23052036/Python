# 986. Interval List Intersections

"""
You are given two lists of closed intervals, firstList and secondList, where 
firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and 
in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed 
interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""

from typing import List


class Solution1:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []

        if len(firstList)==0 or len(secondList)==0:
            return intersection
        
        # writting the O(N^2) solution
        for i in range(len(firstList)):
            matched = False
            start1 = firstList[i][0]
            end1 = firstList[i][1]
            for j in range(len(secondList)):
                start2 = secondList[j][0]
                end2 = secondList[j][1]

                if start1 <= start2 <= end1:
                    intersection.append([start2, min(end2,end1)])
                    matched = True
                elif start2 <= start1 <= end2:
                    intersection.append([start1, min(end2,end1)])
                    matched = True
                elif matched:
                    break
        return intersection
    

    
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersec = []
        i = 0
        j = 0

        while i<len(firstList) and j<len(secondList):
            start1 = firstList[i][0]
            end1 = firstList[i][1]
            start2 = secondList[j][0]
            end2 = secondList[j][1]

            if start1 <= start2 <= end1 or start2 <= start1 <= end2: # intersection case
                intersec.append([max(start1,start2), min(end1,end2)])
            if end1 <= end2:
                i += 1
            else:
                j += 1
        return intersec
