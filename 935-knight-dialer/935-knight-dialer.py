class Solution:
    def knightDialer(self, n: int) -> int:
        totalMove = 0
        MOD = pow(10,9) + 7
        cache = {}
        def findPath(i,j,n):
            if i < 0 or j < 0 or i >= 3 or j >= 4 or (j == 3 and i != 1):
                return 0
            if n == 1:
                return 1
            key = (i,j,n)
            
            if key not in cache:
                cache[key] = (findPath(i - 1,j - 2,n-1) + findPath(i - 2,j - 1,n-1) + findPath(i - 2,j + 1,n-1) + findPath(i - 1,j + 2,n-1) + findPath(i + 1,j - 2,n-1) + findPath(i + 2,j - 1,n-1) + findPath(i + 1,j + 2,n-1) + findPath(i + 2,j + 1,n-1))%MOD

            return cache[key]
        
        for i in range(3):
            for j in range(4):
                totalMove = (totalMove + findPath(i,j,n))
        
        return totalMove % MOD