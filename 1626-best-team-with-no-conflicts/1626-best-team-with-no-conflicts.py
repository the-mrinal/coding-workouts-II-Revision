class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        players = [[a, s] for a, s in zip(ages, scores)]
        players.sort(reverse = True)
        
        dp = [players[i][1] for i in range(n)]

        maxVal = 0
        for i in range(n):
            for j in range(i):
                if players[j][1] >= players[i][1]:
                    dp[i] = max(dp[i],players[i][1] + dp[j])
            maxVal = max(maxVal,dp[i])
        
        return maxVal