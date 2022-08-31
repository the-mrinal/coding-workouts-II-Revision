class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        
        def dfs(x,y):
            que = deque()
            que.append([x,y])
            
            def isNotValid(a,b):
                if a < 0 or b < 0 or a >= m or b >= n or grid[a][b] != "1":
                    return True
                return False
            
            
            while que:
                curr_x,curr_y = que.popleft()
                
                for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                    n_x = a + curr_x
                    n_y = b + curr_y
                    if isNotValid(n_x,n_y):
                        continue
                    grid[n_x][n_y] = "2"
                    que.append([n_x,n_y])
                
        
        count =  0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
                    
        return count