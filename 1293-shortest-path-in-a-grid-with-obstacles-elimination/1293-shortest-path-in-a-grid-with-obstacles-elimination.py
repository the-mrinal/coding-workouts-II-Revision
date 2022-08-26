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
            
            if (row == m -1 and col == n - 1):
                return steps
            
            # explore the four directions in the next step
            for new_row, new_col in [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]:
                # if (new_row, new_col) is within the grid boundaries
                if (0 <= new_row < m) and (0 <= new_col < n):
                    new_eliminations = obs + grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations)
                    # add the next move in the queue if it qualifies
                    if new_eliminations <= k and new_state not in visited:
                        visited.add(new_state)
                        que.append([new_row,new_col,new_eliminations,steps + 1])
        
        return -1
        