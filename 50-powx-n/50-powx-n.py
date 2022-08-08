class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}
        def helper(base,power):
            if power == 1:
                return base
            if power == 0:
                return 1
            if (base,power) in cache:
                return cache[(base,power)]
            
            mid = power // 2
            otherMid = power - mid
            
            cache[(base,power)] =  helper(base,mid) * helper(base,otherMid)
            
            return cache[(base,power)]
        
        if n < 0:
            n = -n
            x = 1/x
        
        
        return helper(x,n)