class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        
        def condition(x):
            out = 0
            ind = 0
            for w in buckets:
                if w > x:
                    out += (w - x)
                else:
                    ind += (x - w)
            if (out - (out * (loss/100))) >= ind:
                return False
            return True
        
        left = min(buckets)
        right = max(buckets)
        
        ellipsion = 10**-5
        
        while right - left > ellipsion: # till the diff beetween them is greater than 0.00005
            mid = float(left + (right - left) / 2)
            
            if condition(mid):
                right = mid
            else:
                left = mid
        
        return left
        
