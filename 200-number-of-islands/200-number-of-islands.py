class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(root):
            que = deque()
            que.append(root)
            grid[root[0]][root[1]] = "0"
            while que:
                x,y = que.popleft()
                
                for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                    n_x = a + x
                    n_y = b + y
                    if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or grid[n_x][n_y] == "0":
                        continue
                        
                    grid[n_x][n_y] = "0"
                    que.append((n_x,n_y))
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs((i,j))
                    count += 1
        
        return count