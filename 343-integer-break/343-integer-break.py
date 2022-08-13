class Solution:
    def integerBreak(self, n: int) -> int:
        
        cache = {}
        
        def findMaxP(index,k):
            if index < 0:
                return float('-inf')
            
            if index == 0:
                if k == 2:
                    return 1
                return 0
            key = (index,k)
            
            if key not in cache:
                ans = 0
                for i in range(1,n + 1):
                    ans = max(ans,findMaxP(index - i,min(k+1,2))*i)
                cache[key] = ans
            
            
            return cache[key]
        
        findMaxP(n,0)
        return cache[(n,0)]
        