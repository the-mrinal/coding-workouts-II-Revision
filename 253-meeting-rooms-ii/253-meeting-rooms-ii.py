class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        countMap = defaultdict(int)
        
        for st,end in intervals:
            countMap[st] += 1
            countMap[end] -= 1
        
        keys = list(countMap.keys())
        keys.sort()
        minRoom = 0
        currRoom = 0
        for k in keys:
            currRoom += countMap[k]
            minRoom = max(minRoom,currRoom)
        
        return minRoom