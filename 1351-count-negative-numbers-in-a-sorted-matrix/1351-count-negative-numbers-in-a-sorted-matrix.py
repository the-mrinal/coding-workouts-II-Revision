class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        
        def condition(index,row):
            if grid[row][index] < 0:
                return True
            return False
        
        def bSearch(left,right,row):
            
            while left < right:
                mid = left + (right - left) // 2
                
                if condition(mid,row):
                    right = mid
                else:
                    left = mid + 1
            
            return len(grid[0]) - left if grid[row][left] < 0 else 0
        
        for i in range(len(grid)):
            count += bSearch(0,len(grid[0]) - 1,i)
        
        return count