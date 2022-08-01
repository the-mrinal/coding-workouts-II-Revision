class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(root):
            stack = [root]
            
            while stack:
                x,y = stack.pop()
                
                for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                    n_x = x + a
                    n_y = y + b
                    
                    if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or grid[n_x][n_y] == 1:
                        continue
                    grid[n_x][n_y] = 1
                    stack.append((n_x,n_y))
        
        for i in range(n):
            if grid[0][i] == 0:
                grid[0][i] = 1
                dfs((0,i))
            if grid[m - 1][i] == 0:
                grid[m-1][i] = 1
                dfs((m-1,i))
        
        for i in range(m):
            if grid[i][0] == 0:
                grid[i][0] = 1
                dfs((i,0))
            if grid[i][n - 1] == 0:
                grid[i][n-1] = 1
                dfs((i,n-1))
        count = 0
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 0:
                    count += 1
                    # print(i,j)
                    dfs((i,j))
        
        return count