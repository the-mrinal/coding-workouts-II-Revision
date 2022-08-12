class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        
        n = len(prices)
        curr_min = prices[0]
        profits = []
        max_profit = 0
        for i in range(n):
            curr_min = min(curr_min,prices[i])
            max_profit = max(max_profit,prices[i] - curr_min)
            profits.append(max_profit)
        
        total_max = 0
        curr_max = prices[-1]
        max_profit = 0
        
        for i in range(n-1,-1,-1):
            curr_max = max(curr_max,prices[i])
            max_profit = max(max_profit,curr_max - prices[i])
            total_max = max(total_max,max_profit + profits[i])
        
        return total_max
        
        
        
#         cache = {}
#         def findMaxStock(index,bought,count):
#             if index == n:
#                 return 0
#             if count == 2:
#                 return 0
#             key = (index,bought,count)
#             if key not in cache:
#                 ans1 = 0
#                 ans2 = 0
#                 if bought:
#                     ans1 = prices[index] + findMaxStock(index + 1,False,count + 1)
#                 else:
#                     ans1 = -prices[index] + findMaxStock(index + 1,True,count)

#                 ans2 = findMaxStock(index + 1,bought,count)

#                 cache[key] = max(ans1,ans2)

#             return cache[key]
        
#         return findMaxStock(0,False,0)