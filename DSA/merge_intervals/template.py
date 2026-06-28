class Solution1:

    def merge_with_extra_space(self,intervals):
        intervals.sort(key = lambda x:x[0])
        new_intervals=[]
        new_intervals.append(intervals[0])

        for i in range(1,len(intervals)):
            if intervals[i][0]<=new_intervals[-1][1]: # merge intervlas
                new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
            else:
                new_intervals.append(intervals[i])
        return intervals
    
    
    def mer_without_space(self,intervals):
        intervals.sort(key=lambda x:x[0])
        write=0

        for i in range(1,len(intervals)):
            if intervals[i][0] <= intervals[write][1]: # merge intervals
                intervals[write][1] = max(intervals[write][1], intervals[i][1])
            else:
                write += 1
                intervals[write] = intervals[i]
        return intervals[:write+1]
