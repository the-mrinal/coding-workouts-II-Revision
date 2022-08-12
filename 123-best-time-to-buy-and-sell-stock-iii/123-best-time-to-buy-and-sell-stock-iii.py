class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}
        def findMaxStock(index,bought,count):
            if index == n:
                return 0
            if count == 2:
                return 0
            key = (index,bought,count)
            if key not in cache:
                ans1 = 0
                ans2 = 0
                if bought:
                    ans1 = prices[index] + findMaxStock(index + 1,False,count + 1)
                else:
                    ans1 = -prices[index] + findMaxStock(index + 1,True,count)

                ans2 = findMaxStock(index + 1,bought,count)

                cache[key] = max(ans1,ans2)

            return cache[key]
        
        return findMaxStock(0,False,0)