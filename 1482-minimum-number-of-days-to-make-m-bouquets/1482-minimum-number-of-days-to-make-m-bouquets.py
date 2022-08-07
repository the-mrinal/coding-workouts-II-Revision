class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        n = len(bloomDay)
        if m*k > n:
            return -1
        
        def condition(bloom):
            flowers = 0
            bouq = 0
            for days in bloomDay:
                if days > bloom:
                    flowers = 0
                else:
                    flowers = flowers + 1
                    bouq += flowers // k
                    flowers = flowers % k

            return bouq >= m
    
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left