# -------------------------------------------------------------------------
# NOTE:
# The following approach DOES NOT solve the "Meeting Rooms II" problem.
#
# Instead, it solves the following problem:
#
# Given a set of intervals, merge all directly or transitively overlapping
# intervals into groups. Count how many original intervals belong to each
# merged group, and return the size of the largest group.
#
# Example:
#
# Intervals:
# [1,3], [2,5], [4,6], [8,9], [9,10]
#
# Merged Groups:
# Group 1 -> [1,6]  (contains 3 original intervals)
# Group 2 -> [8,10] (contains 2 original intervals)
#
# Output: 3
#
# Why this fails for Meeting Rooms II:
# Merging intervals loses the individual meeting end times. Once intervals
# are merged, it is impossible to know when a room becomes free, so this
# approach counts the number of intervals in a connected overlapping group
# rather than the maximum number of simultaneously active meetings.
# -------------------------------------------------------------------------

class Solution:
    def minMeetingRooms(self, start, end):
        
        if len(start)==0:
            return 0
        
        dict = {}
        new_interval = []
        
        for i in range(len(start)):
            new_interval.append([start[i],end[i]])
        new_interval.sort(key = lambda x:x[0])
        
        write = 0
        dict[new_interval[0][0]] = 1
        maxi = 1
        
        for i in range(1,len(new_interval)):
            start1 = new_interval[i][0]
            end1 = new_interval[i][1]
            
            if start1 <= new_interval[write][1]: # conflict time
                # first update the new interval
                new_interval[write][1] = max(new_interval[write][1], end1)
                dict[new_interval[write][0]] = dict.get(new_interval[write][0],0) + 1
                maxi = max(maxi,dict.get(new_interval[write][0]))
            else:
                write += 1
                new_interval[write] = new_interval[i]
                dict[start1] = 1
        return maxi
            
        
