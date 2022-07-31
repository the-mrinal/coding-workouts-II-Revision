class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        directions = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        
        que = deque()
        
        que.append([0,0,1])
        visited = set()
        visited.add((0,0))
        while que:
            x,y,cost = que.popleft()
            if x == n - 1 and y == n - 1:
                return cost
            
            for a,b in directions:
                n_x = x + a
                n_y = y + b
                
                if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n or (n_x,n_y) in visited or grid[n_x][n_y] == 1:
                    continue
                que.append([n_x,n_y,cost + 1])
                visited.add((n_x,n_y))
        
        return -1
                