class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        minHeap = []
        for st,en in points:
            heappush(minHeap,[en,st])
        
        count = 1
        curr_max = minHeap[0][0]
        while minHeap:
            en,st = heappop(minHeap)
            
            if st > curr_max:
                count += 1
                curr_max = en
        
        return count