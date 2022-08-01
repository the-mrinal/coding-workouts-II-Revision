class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        curr = 0
        
        for i in range(len(prices) - 1):
            curr = max(0,curr + (prices[i+1] - prices[i]))
            maxSoFar = max(curr,maxSoFar)
        return maxSoFar
        