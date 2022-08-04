class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        count = 0
        n = len(s)
        def validate(s,locked,CURR):
            bal,wild = 0,0
            for i in range(n):
                if locked[i] == "1":
                    bal += 1 if CURR == s[i] else -1
                else:
                    wild += 1
                
                
                if wild + bal < 0:
                    return False
            return bal <= wild
        
        return n % 2 == 0 and validate(s,locked,'(') and validate(s[::-1],locked[::-1],')')