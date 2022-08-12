class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = {}
        def countWays(index):
            nonlocal n
            
            if index <= n - 1 and s[index] == '0':
                return 0
        
            if index == n or index == n - 1:
                return 1
            
            if index not in cache:
                ans1 = 0
                ans2 = 0
                if index < n - 1 and int(s[index:index + 2]) <= 26 and s[index] != '0':
                    ans1 =  countWays(index + 2)

                ans2 = countWays(index + 1)
                cache[index] = ans1 + ans2 
            
            return cache[index]
        
        
        return countWays(0)