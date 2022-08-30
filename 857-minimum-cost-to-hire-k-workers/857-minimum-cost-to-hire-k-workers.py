from fractions import Fraction
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted((Fraction(w/q),q,w) for q,w in zip(quality,wage))
        
        maxHeap = []
        sumq = 0
        ans = float('inf')
        
        for ratio,q,w in workers:
            heapq.heappush(maxHeap,-q)
            
            sumq += q
            
            if len(maxHeap) > k:
                sumq += heapq.heappop(maxHeap)
            
            if len(maxHeap) == k:
                ans  = min(sumq*ratio,ans)
        
        return ans