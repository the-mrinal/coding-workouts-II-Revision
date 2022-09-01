class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n - 2
        
        def condition(mid):
            if nums[mid + 1] >= nums[mid]:
                return False
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left