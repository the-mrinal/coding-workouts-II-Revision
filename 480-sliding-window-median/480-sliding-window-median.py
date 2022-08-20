class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        
        def rebalance_heaps():
            if len(self.maxHeap) > len(self.minHeap) + 1:
                heappush(self.minHeap,-heappop(self.maxHeap))
            elif len(self.minHeap) > len(self.maxHeap):
                heappush(self.maxHeap,-heappop(self.minHeap))
        
        def remove_elem(target):
            targetHeap = None
            if target <= -self.maxHeap[0]:
                targetHeap = self.maxHeap
                target = - target
            else:
                targetHeap = self.minHeap
            index = targetHeap.index(target)
            targetHeap[index] = targetHeap[-1]
            
            del targetHeap[-1]
            
            if index < len(targetHeap):
                heapq._siftup(targetHeap,index)
                heapq._siftdown(targetHeap,0,index)
                
        n = len(nums)
        res = [0.0 for _ in range(n - k + 1)]
        for i in range(n):
            if not self.maxHeap or -self.maxHeap[0] >= nums[i]:
                heappush(self.maxHeap,-nums[i])
            else:
                heappush(self.minHeap,nums[i])
                
            rebalance_heaps()
            
            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    value = -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
                else:
                    value = -self.maxHeap[0]
            
                res[i -k + 1] = value
                
                remove_elem(nums[i - k + 1])
                
                rebalance_heaps()
        
        return res