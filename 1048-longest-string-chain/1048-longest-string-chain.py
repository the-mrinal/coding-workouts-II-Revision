'''
dp = defaultdict(int)

for i in len(n):
    dp[words[i]] = max([(dp[:i]+dp[i+1:]) + 1 for j in range(words)])

return max(dp.values())

'''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        words.sort(key=len)
        
        for w in words:
            dp[w] = max([(dp[w[:i] + w[i+1:]]) + 1 for i in range(len(w))])
        
        # print(dp)
        return max(dp.values())
    