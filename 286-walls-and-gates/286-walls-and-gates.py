class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        que = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    que.append([i,j,0])
        INF = 2147483647
        visited = set()
        
        def isNotValid(x,y):
            if x < 0 or x >= m or y < 0 or y >= n or (x,y) in visited or rooms[x][y] < INF:
                return True
            return False
        
        while que:
            x,y,level = que.popleft()
            
            if rooms[x][y] == INF:
                rooms[x][y] = level
            
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                n_x = x + a
                n_y = y + b
                if isNotValid(n_x,n_y):
                    continue
                visited.add((n_x,n_y))
                que.append([n_x,n_y,level + 1])