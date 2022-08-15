class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n + 1)]
        
        for i in range(n - 1,-1,-1):
            for isHold in range(2):
                doNothing = dp[i + 1][isHold]
                doSomething = None
                if isHold:
                    doSomething = prices[i] + dp[i + 1][0] - fee
                else:
                    doSomething = -prices[i] + dp[i + 1][1]
                
                dp[i][isHold] = max(doNothing,doSomething)
        
        return dp[0][0]