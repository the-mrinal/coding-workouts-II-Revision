class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxSize = 0
        maxVal = ""
        
        def findP(left,right):
            nonlocal maxSize,maxVal,n
            currMax = 0
            currVal = ""
            
            while left >= 0 and right < n and s[left] == s[right]:
                if left != right:
                    currMax += 2
                else:
                    currMax += 1
                left -=1 
                right += 1
            
            if currMax > maxSize:
                maxSize = currMax
                maxVal = s[left +1 : right]
            
        
        for i in range(n):
            findP(i,i)
            findP(i,i+1)
        
        return maxVal