class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        que =deque()
        dist =[[-1 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append([i,j,0])
                    
        visited = set()
        
        while que:
            x,y,depth = que.popleft()
            
            if dist[x][y] == -1:
                dist[x][y] = depth
                
            visited.add((x,y))
            
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                n_x = x + a
                n_y = y + b
                
                if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or dist[n_x][n_y] != -1 or (n_x,n_y) in visited:
                    continue
                    
                
                que.append([n_x,n_y,depth + 1])
                
        
        return dist