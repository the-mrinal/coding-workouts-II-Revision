class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        n = len(s)
        
        dp = [False]*n
        
        for i in range(n):
            for w in words:
                if (i + 1 >= len(w)) and (i + 1 == len(w) or dp[i - len(w)]):
                    if s[i - len(w)+1:i+1] == w:
                        dp[i] = True
        
        return dp[n-1]