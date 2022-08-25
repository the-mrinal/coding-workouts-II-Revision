class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dp = [0 for _ in range(1950,2051)]
        
        for b,d in logs:
            dp[b - 1950]  += 1
            dp[d - 1950] -= 1
        maxDp = dp[0]
        year = 1950
        for i in range(1951,2051):
            dp[i - 1950] += dp[i-1 - 1950]
            if maxDp < dp[i- 1950]:
                maxDp = dp[i- 1950]
                year = i 
        return year