class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        que = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    que.append([i,j,0,[(i,j)]])
        
        while que:
            x,y,index,visited = que.pop()
            
            if index == len(word) - 1:
                return True
            
            for a,b in directions:
                n_x = x + a
                n_y = y + b
                if (n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or (n_x,n_y) in visited or board[n_x][n_y] != word[index + 1]):
                    continue
                que.append([n_x,n_y,index + 1,visited + [(n_x,n_y)]])
        
        return False
            