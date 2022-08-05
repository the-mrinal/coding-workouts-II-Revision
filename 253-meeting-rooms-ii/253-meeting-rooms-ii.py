class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap = []
        # intervals.sort()
        for index,val in enumerate(intervals):
            heappush(minHeap,[val[0],1])
            heappush(minHeap,[val[1],-1])       
            
        
        count = 0
        maxCount = 0
        while minHeap:
            curr,state = heappop(minHeap)
            
            count += state
            maxCount = max(count,maxCount)
        
        return maxCount