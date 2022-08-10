class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        dp = [0 for _ in range(n+1)]
        
        dp[1] = k
        
        
        dp[2]= k * k
        
        same ,diff = k,k*(k-1)
        
        for i in range(3,n+1):
            same,diff = diff,(k-1)*(same + diff)
            dp[i] = same + diff
        return dp[n]