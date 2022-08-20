class Solution:
    def __init__(self):
        self.minCapHeap = []
        self.maxAvailProfit = []
    
    
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = 0
        
        for index in range(len(capital)):
            heappush(self.minCapHeap,[capital[index],index])
        
        availCapital = w
        
        
        
        for i in range(k):
            while self.minCapHeap and self.minCapHeap[0][0] <= availCapital:
                _,index = heappop(self.minCapHeap)
                heappush(self.maxAvailProfit,-profits[index])
            
            if not self.maxAvailProfit:
                break
            availCapital += -heappop(self.maxAvailProfit)
        
        return availCapital