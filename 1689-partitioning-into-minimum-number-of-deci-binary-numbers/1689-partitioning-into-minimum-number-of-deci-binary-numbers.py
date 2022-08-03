class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for num in n:
            res = max(res,int(num))
        
        return res