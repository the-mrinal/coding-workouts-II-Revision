class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev = 1
        curr = 2
        
        for i in range(3,n + 1):
            temp = curr
            curr = curr + prev
            prev = temp
        
        return curr