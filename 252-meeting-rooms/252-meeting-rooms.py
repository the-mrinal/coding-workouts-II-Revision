class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x:x[1])
        
        
        currMax = intervals[0][1]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] >= currMax:
                currMax = intervals[i][1]
            else:
                return False
        
        return True