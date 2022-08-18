class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        
        if m*k > len(bloomDay):
            return -1
        
        def condition(targetDay):
            bouq = 0
            flower = 0
            for day in bloomDay:
                if day > targetDay:
                    flower = 0
                else:
                    flower += 1
                    bouq += flower // k
                    flower = flower % k

            return bouq >= m
        
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        
        return left
                    