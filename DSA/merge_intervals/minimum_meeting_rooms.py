"""
Given two arrays start[] and end[] such that start[i] is the starting time of ith meeting and end[i] is the ending 
time of ith meeting. Return the minimum number of rooms required to attend all meetings.

Note: A person can also attend a meeting if it's starting time is same as the previous meeting's ending time.

Examples:

Input: start[] = [1, 10, 7], end[] = [4, 15, 10]
Output: 1
Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings in a 
single room.

Input: start[] = [2, 9, 6], end[] = [4, 12, 10]
Output: 2
Explanation: 1st and 2nd meetings at one room but for 3rd meeting one another room required.

Constraints:
1 ≤ start.size() = end.size() ≤ 105
0 ≤ start[i] < end[i] ≤ 106
"""

class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        start.sort()
        end.sort()
        
        ptr1 = 0
        ptr2 = 0
        maxi = 0
        ans = 0
        while ptr1<len(start) or ptr2<len(end):
            if ptr1<len(start) and ptr2<len(end):
                if start[ptr1] < end[ptr2]: # if we put a <= here the solution will fail find out why ? easy!!!
                    ptr1 += 1
                    maxi += 1
                else:
                    ptr2 += 1
                    maxi -= 1
            elif ptr1<len(start):
                ptr1 += 1
                maxi += 1
            elif ptr2<len(end):
                ptr2 += 1
                maxi -= 1
            ans = max(ans,maxi)
        return ans
