class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = grid[0]
        curr = [0 for _ in range(n)]
        
        for i in range(1,m):
            for j in range(n):
                value = float('inf')
                for k in range(n):
                    value = min(value,prev[k] + moveCost[grid[i - 1][k]][j])
                curr[j] = value + grid[i][j]
            prev = curr
            curr = [0]*n
        return min(prev)