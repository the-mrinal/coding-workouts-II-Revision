class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        k = len(costs[0])
        
        dp = [[0]*k for _ in range(2)]
        
        for i in range(k):
            dp[0][i] = costs[0][i]
        
        
        
        for i in range(1,n):
            for j in range(k):
                dp[i%2][j] = costs[i][j] + min(dp[(i - 1)%2][:j]+dp[(i-1)%2][j+1:])
        
        return min(dp[(n - 1)%2])