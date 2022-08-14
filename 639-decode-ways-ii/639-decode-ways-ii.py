class Solution:
    def numDecodings(self, S: str) -> int:
        
        e,eOne,eTwo = 1,0,0
        
        for c in S:
            if c == '*':
                f0 = 9*e + 9*eOne + 6*eTwo
                f1 = e
                f2 = e
            else:
                f0 = (c > '0') * e + eOne + (c <= '6') * eTwo
                
                f1 = (c == '1') * e
                f2 = (c =='2') * e
            e,eOne,eTwo = f0 %(10**9 + 7),f1,f2
        
        return e