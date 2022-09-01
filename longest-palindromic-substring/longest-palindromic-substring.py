class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxCount = 0
        maxString = ""
        n = len(s)
        if n <= 1:
            return s
        
        def findLongestP(i,j):
            nonlocal maxCount,maxString
            count = 0
            while i >= 0 and j < n and s[i] == s[j]:
                if i == j:
                    count += 1
                else:
                    count += 2
                i -= 1
                j += 1
            
            if maxCount < count:
                maxCount = count
                print(i,j,s[i +1:j])
                maxString = s[i +1:j]
            
        for i in range(n-1):
            findLongestP(i,i)
            findLongestP(i,i+1)
        return maxString
            