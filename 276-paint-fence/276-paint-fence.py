class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n <= 2:
            return k ** n
        dp = [0 for _ in range(n + 1)]
        dp[1] = k ** 1
        dp[2] = (k ** 2) 
        for i in range(3,n + 1):
            dp[i] = (k-1)*(dp[i - 1] + dp[i -2])
        
        return dp[n]
        