class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        minHeap = []
        for st,end in intervals:
            heappush(minHeap,[end,st])
            
        count = 1
        currMax = minHeap[0][0]
        heappop(minHeap)
        
        while minHeap:
            end,st = heappop(minHeap)
            
            if st >= currMax:
                count += 1
                currMax = end
        
        return len(intervals) - count