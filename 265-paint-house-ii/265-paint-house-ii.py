class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        k = len(costs[0])
        
        dp = [[0]*k for _ in range(n)]
        
        for i in range(k):
            dp[0][i] = costs[0][i]
        
        
        
        for i in range(1,n):
            for j in range(k):
                dp[i][j] = costs[i][j] + min(dp[i - 1][:j]+dp[i-1][j+1:])
        
        return min(dp[n - 1])