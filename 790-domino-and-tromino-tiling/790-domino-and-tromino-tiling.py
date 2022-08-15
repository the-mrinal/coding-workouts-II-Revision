class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        MOD = 10**9 + 7
        for i in range(4,n + 1):
            dp[i] = ((2*dp[i - 1]) % MOD + dp[i - 3]%MOD)%MOD
        
        return dp[n]