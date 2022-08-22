class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        
        dp = [[0 for _ in range(n2)] for _ in range(n1)]
        
            
        
        for i in range(n1):
            for j in range(n2):
                if i > 0 and j > 0 and word1[i] == word2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                elif word1[i] == word2[j]:
                    dp[i][j] = 1
                dp[i][j] = max(dp[i][j],dp[i-1][j],dp[i][j - 1])
        return  n1 + n2 - 2*(dp[n1-1][n2-1])