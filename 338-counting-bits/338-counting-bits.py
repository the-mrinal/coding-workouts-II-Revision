class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n +1)
        x = 0
        b = 1
        
        while b <= n:
            while x < b and x + b <= n:
                ans[x + b] = ans[x] + 1
                x += 1
            x = 0
            b = 2*b
        return ans