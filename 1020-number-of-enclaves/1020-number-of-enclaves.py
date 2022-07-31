'''
return the no if ones that disconnected form boundary

loop throght all the boundary and put all the ones in que.

now try to traverse que in all directions if found turn it into 0

after doing this count - no of ones



'''


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        que = deque()
        m = len(grid)
        n = len(grid[0])
        
       # top,bottom boundary
        for i in range(n):
            if grid[0][i] == 1:
                que.append([0,i])
            if grid[m - 1][i] == 1:
                que.append([m - 1,i])
        
        # left,right
        
        for i in range(m):
            if grid[i][0] == 1:
                que.append([i,0])
            if grid[i][n - 1] == 1:
                que.append([i,n-1])
        
        while que:
            x,y = que.popleft()
            
            grid[x][y] = 0
            
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                n_x = x + a
                n_y = y + b
                
                if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or grid[n_x][n_y] == 0 or [n_x,n_y] in que:
                    continue
                
                que.append([n_x,n_y])
        
        # print(grid)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                
        return count