class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        que = deque()
        if entrance:
            que.append(entrance + [0])
        
        visited = set()
        visited.add((entrance[0],entrance[1]))
        
        while que:
            x,y,st = que.popleft()
            
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                n_x = x + a
                n_y = y + b
                
                if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or (n_x,n_y) in visited or maze[n_x][n_y] == '+':
                    continue
                if n_x == 0 or n_y == 0 or n_x == m - 1 or n_y == n - 1:
                    return st + 1
                visited.add((n_x,n_y))
                que.append([n_x,n_y,st + 1])
        
        return -1