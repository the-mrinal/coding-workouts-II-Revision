class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = min(a,b,c)
        right = 10**10
        
        ab = (a*b) // math.gcd(a,b) #find lcm ab
        bc = (b*c) // math.gcd(b,c)
        ac = (a*c) // math.gcd(a,c)
        abc = (ab*c) // math.gcd(ab,c)
        
        def condition(ugly):
            num = ugly//a + ugly // b + ugly // c - ugly //ab - ugly//ac - ugly // bc +  ugly/abc
            return num >= n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        