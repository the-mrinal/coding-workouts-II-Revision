class Solution:
    def minDifficulty(self, jD: List[int], d: int) -> int:
        n = len(jD)
        cache = {}
        def dfs(day,jobIndex):
            if day == d:
                return max(jD[jobIndex:])
            
            key = (day,jobIndex)
            
            if key not in cache:
                currMax = 0
                j = n - (d - day)
                ansMin = float('inf')
                for i in range(jobIndex,j):
                    currMax = max(currMax,jD[i])
                    ansMin = min(ansMin,currMax + dfs(day + 1,i+1))
                cache[key] = ansMin
            return cache[key]
        
        ans = dfs(1,0)
        return ans if ans < float('inf') else -1