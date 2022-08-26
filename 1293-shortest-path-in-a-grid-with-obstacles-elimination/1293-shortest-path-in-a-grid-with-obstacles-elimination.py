# x,y,obs,path found
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if k >= m + n - 2:
            return m + n - 2
        
        que = deque()
        if grid:
            que.append([0,0,0,0])
        visited = set()
        visited.add((0,0,0))
        while que:
            row,col,obs,steps = que.popleft()
            
            if (row == m -1 and col == n - 1) and obs <= k:
                return steps
            
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                n_x = row + a
                n_y = col + b
                if n_x < 0 or n_y < 0 or n_x >= m or n_y >= n:
                    continue
                new_obs = obs + grid[n_x][n_y]
                if new_obs <= k and (n_x,n_y,new_obs) not in visited:
                    visited.add((n_x,n_y,new_obs))
                    que.append((n_x,n_y,new_obs,steps + 1))
        
        return -1
        
        
#             if (0 <= n_x < m) and (0 <= n_y < n):
#                     new_obs = obs + grid[n_x][n_y]
#                     if new_obs <= k and (n_x,n_y,new_obs) not in visited:
#                         visited.add((n_x,n_y,new_obs))
#                         que.append([n_x,n_y,new_obs,steps + 1])
        