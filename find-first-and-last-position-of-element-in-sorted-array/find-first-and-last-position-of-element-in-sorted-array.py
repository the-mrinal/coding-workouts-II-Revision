class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        if not nums:
            return [-1,-1]
        
        def findLeft():
            left = 0
            right = n - 1
            
            def conditionLeft(mid):
                if nums[mid] >= target:
                    return True
                return False
            
            while left < right:
                mid = left + (right - left) // 2
                
                if conditionLeft(mid):
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        def findRight():
            left = 0
            right = n - 1

            def conditionRight(mid):
                if nums[mid] > target:
                    return True
                return False

            while left < right:
                mid = left + (right - left + 1) // 2

                if conditionRight(mid):
                    right = mid - 1
                else:
                    left = mid

            return left
        
        left = findLeft()
        right = findRight() if nums[left] == target else -1
        
        left = -1 if nums[left] != target else left
        
        return [left,right]
        
        