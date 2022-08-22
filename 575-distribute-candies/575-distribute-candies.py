class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        total = len(candyType)
        target = total // 2
        
        n = set(candyType)
        size = len(n)
        
        
        if size <= target:
            return size
        return target