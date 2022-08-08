class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        
        n = len(grid[0])
        
        dp = [[0 for y in range(n)] for x  in range(m)]
        
        dp[0][0] = 1 if grid[0][0] == 0 else 0

        
        for i in range(1,n):
            dp[0][i] = 1 if grid[0][i] == 0 and dp[0][i - 1] == 1 else 0
        
        for i in range(1,m):
            dp[i][0] = 1 if grid[i][0] == 0 and dp[i - 1][0] == 1 else 0
        
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

                
        # print(dp)
        return dp[m-1][n-1]