class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cache = {}
        def dfs(index,bought):
            if index == n:
                return 0
            key = (index,bought)
            if key not in cache:
                if bought:
                    ans1 = prices[index] - fee + dfs(index + 1,False)
                elif bought == False:
                    ans1 = -prices[index] + dfs(index + 1,True)

                ans2 = dfs(index + 1,bought)
                cache[key] = max(ans1,ans2)
                
                
            return cache[key]
        
        dfs(0,False)
        return cache[(0,False)]
            