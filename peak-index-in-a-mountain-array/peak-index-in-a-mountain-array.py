class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 1
        right = n - 2
        
        def condition(mid):
            if arr[mid + 1] >= arr[mid]:
                return False
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left