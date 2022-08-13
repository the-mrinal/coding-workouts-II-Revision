class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        cache = {}
        def findMaxProfit(index,bought,cooldown):
            if index == n:
                return 0
            
            key = (index,bought,cooldown)
            
            if key not in cache:
                ans1 = 0
                ans2 = 0
                if bought and cooldown == 0:
                    ans2 = prices[index] + findMaxProfit(index + 1,False,1)
                elif not bought and cooldown == 0:
                    ans2 = -prices[index] + findMaxProfit(index + 1,True,0)

                ans1 = findMaxProfit(index + 1,bought,max(0,cooldown - 1))
                # print(a)
                cache[key] = max(ans1,ans2)
            
            return cache[key]
        
        return findMaxProfit(0,False,0)