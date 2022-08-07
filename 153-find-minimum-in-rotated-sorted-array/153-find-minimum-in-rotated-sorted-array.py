class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        
        right = n - 1
        
        def condition(mid):
            if nums[0] > nums[mid] or nums[0] < nums[-1]:
                if nums[mid] < nums[mid + 1]:
                    return True
                else:
                    return False
            else:
                return False
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return nums[left]