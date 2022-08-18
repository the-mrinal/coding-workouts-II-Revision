# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findMountain(self,nums,size):
        left = 1
        right = size - 2
        while left < right:
            mid = left + (right - left + 1) //  2

            curr = nums.get(mid)
            prev = nums.get(mid - 1)

            if curr < prev:
                right = mid - 1
            else:
                left = mid
        
        return left



    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        n = mountain_arr.length()
        m_index = self.findMountain(mountain_arr,n)
        t_index = self.orderAgnosticBSearch(0,m_index - 1,target,mountain_arr)
        if t_index == -1:
            t_index = self.orderAgnosticBSearch(m_index,n-1,target,mountain_arr)
        
        return t_index

    def orderAgnosticBSearch(self,start,end,target,nums):
        left = start
        right = end
        start_elem = nums.get(start)
        end_elem = nums.get(end)
        
        def condition(mid):
            mid_e = nums.get(mid)
            if mid_e > start_elem or end_elem > mid_e:
                if mid_e >= target:
                    return True
                return False
            else:
                if mid_e <= target:
                    return True
                return False    
        
        
        while left < right:

            mid = left + (right - left) // 2
            curr = nums.get(mid)
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
            
        # print(left)
        return left if nums.get(left) == target else -1

        