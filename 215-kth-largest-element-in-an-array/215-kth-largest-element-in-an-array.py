class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        
        n = len(nums)
        
        smallest_k = n - k + 1
        
        for index ,val in enumerate(nums):
            if index < smallest_k:
                heappush(maxHeap,(-val,index))
            elif index >= smallest_k and val < -maxHeap[0][0]:
                heappop(maxHeap)
                heappush(maxHeap,(-val,index))
        
        return -maxHeap[0][0]