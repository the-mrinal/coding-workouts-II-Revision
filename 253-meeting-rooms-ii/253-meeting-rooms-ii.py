class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap = []
        
        for start,end in intervals:
            heappush(minHeap,[start,1])
            heappush(minHeap,[end,-1])
        
        count = 0
        maxCount = 0
        while minHeap:
            curr,state = heappop(minHeap)
            
            count += state
            
            maxCount = max(maxCount,count)
            
        
        return maxCount