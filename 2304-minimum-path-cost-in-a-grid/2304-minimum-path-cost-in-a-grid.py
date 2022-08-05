class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = grid[0]
        curr = [0 for _ in range(n)]
        
        for i in range(1,m):
            for j in range(n):
                minVal = float('inf')
                for k in range(n):
                    minVal = min(minVal,moveCost[grid[i - 1][k]][j] + prev[k])
                curr[j] = minVal + grid[i][j]
            prev = curr
            curr = [0]*n
        return min(prev)