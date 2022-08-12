class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        maxSoFar = 0
        
        for index in range(len(prices) - 1):
            currMax = max(0,currMax + (prices[index + 1] - prices[index]))
            
            maxSoFar = max(currMax,maxSoFar)
        
        return maxSoFar