class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        left = min(buckets)
        right = max(buckets)
        
        elipsion = 10 ** -5
        
        def condition(target):
            out = 0
            ind = 0
            for num in buckets:
                if num > target:
                    out += (num - target)
                else:
                    ind += (target - num)
            
            if out - (out * (loss/100)) >= ind:
                return False
            return True
        
        
        while right - left > elipsion:
            mid = float(left + (right - left) / 2)
            
            if condition(mid):
                right = mid
            else:
                left = mid
        
        return left