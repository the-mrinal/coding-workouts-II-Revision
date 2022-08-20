class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}
        def dfs(power):
            if power == 1:
                return x
            elif power == 0:
                return 1
            elif power == 2:
                return x * x
            if power not in cache:
                mid = power // 2
                otherMid = power - mid
                ans1 = dfs(mid)
                ans2 = dfs(otherMid)
                cache[power] = ans1 * ans2
            
            return cache[power]
        
        if n < 0:
            x = 1/x
            n = -n
        return dfs(n)
        