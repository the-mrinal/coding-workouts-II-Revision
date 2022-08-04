class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        same = grid[0]
        rev = [1 - val for val in grid[0]]
        
        for g in grid:
            if g != same and g != rev:
                return False
        return True