class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        que = deque()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    que.append([i,j,0])
        maxDepth = -1
        while que:
            x,y,depth = que.popleft()
            
           
            
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                n_x = x + a
                n_y = y + b
                
                if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n or grid[n_x][n_y] != 0:
                    continue
                grid[n_x][n_y] = 1
                maxDepth = max(maxDepth,depth + 1)
                que.append([n_x,n_y,depth + 1])
            
        return maxDepth