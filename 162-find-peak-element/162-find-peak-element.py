class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right = n - 1
        
        def condition(mid):
            # if not 0 and dsc then move 
            if mid > 0 and nums[mid] < nums[mid - 1]: # alternaring asc and dec
                return True
            return False
        
        while left < right:
            mid = left + math.ceil((right - left + 1) / 2)
            
            if condition(mid):
                right = mid - 1
            else:
                left = mid
        
        return left