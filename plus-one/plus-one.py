class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        n = len(digits)
        carry = 1
        for i in range(n -1,-1,-1):
            val = digits[i] + carry
            carry = val // 10
            val = val % 10
            res.appendleft(val)
        
        if carry > 0:
            res.appendleft(carry)
        
        return list(res)