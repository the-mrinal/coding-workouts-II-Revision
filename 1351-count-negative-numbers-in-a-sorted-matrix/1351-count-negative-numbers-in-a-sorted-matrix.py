class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def condition(curr,mid):
            return grid[curr][mid] < 0
        
        def bSearch(si,ei,curr):
            while si < ei:
                mid = si + (ei - si) // 2
                
                if condition(curr,mid):
                    ei = mid
                else:
                    si = mid + 1
            return si
        count = 0
        for i in range(m):
            si = 0
            ei = n
            index = bSearch(si,ei,i)
            if index < 0 or index >= n or grid[i][index] >= 0:
                continue
            count += (n - index)
        
        return count