class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        def condition(mid):
            count = 1
            currVal = 0
            for num in nums:
                currVal += num
                
                if currVal > mid:
                    currVal = num
                    count += 1
                if count > m:
                    return False
            
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left