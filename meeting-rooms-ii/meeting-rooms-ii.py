class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        currRooms = defaultdict(int)
        
        for start,end in intervals:
            currRooms[start] += 1
            currRooms[end] -= 1
        keys = list(currRooms.keys())
        keys.sort()
        
        maxRoom = 0
        curr = 0
        for k in keys:
            curr += currRooms[k]
            maxRoom = max(curr,maxRoom)
        
        return maxRoom