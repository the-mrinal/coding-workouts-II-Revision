class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = (m)*(n)
        
        def condition(mid):
            x = mid // n 
            y = mid % n
            if matrix[x][y] >= target:
                return True
            return False
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
         
        x = left // n 
        y = left % n
        return True if x < m and y < n and matrix[x][y] == target else False