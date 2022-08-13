class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        
        for coin in coins:
            for j in range(coin,amount + 1):
                dp[j] = min(dp[j],dp[j - coin] + 1)
        return dp[amount] if dp[amount] < float('inf') else -1
                
            
        
#         cache = {}
#         def findCount(target):
#             if target == 0:
#                 cache[target] = 0
#                 return 0
#             if target < 0:
#                 return float('inf')
            
#             key = target
            
#             if key not in cache:
#                 ans = float('inf')
#                 for coin in coins:
#                     ans = min(ans,1 + findCount(target - coin))
#                 cache[key] = ans
            
#             return cache[key]
        
#         findCount(amount)
        
#         return cache[amount] if cache[amount] < float('inf') else -1
    