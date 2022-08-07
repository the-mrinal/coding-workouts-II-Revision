class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bSearch(lo,hi):
            print(lo,hi)
            while lo < hi:
                mid = lo + (hi - lo)//2
                print(mid)
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            print(lo)
            return lo if lo < n and nums[lo] == target else -1
        
        n = len(nums)
        
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        
        
        
        
        index = 1
        while index < n and nums[index] > nums[index - 1]:
            index += 1

        if target >= nums[0]:
            return bSearch(0,index - 1)
        return bSearch(index, n - 1)
        