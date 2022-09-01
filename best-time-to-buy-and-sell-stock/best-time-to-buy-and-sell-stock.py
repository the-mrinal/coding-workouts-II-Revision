class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        currMax = 0
        n = len(prices)
        for i in range(n - 1):
            currMax = max(0,currMax + (prices[i + 1] - prices[i]))
            maxSoFar = max(currMax,maxSoFar)
        
        return maxSoFar