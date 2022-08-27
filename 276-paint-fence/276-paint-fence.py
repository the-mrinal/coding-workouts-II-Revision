class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n <= 2:
            return k**(n)
        dp = [0 for _ in range(n+1)]
        dp[0] = k
        dp[1] = k*k
        
        for i in range(2,n):
            dp[i] = (k-1)*(dp[i-1] + dp[i - 2])
            
        
        
        return dp[n - 1]