class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [i**2 for i in range(int(n ** 0.5) + 1)]
        que = deque()
        que.append([n,1])
        
        curr_level = 1
        
        while que:
            curr,level = que.popleft()
            
            curr_level = level
            
            for sq in dp:
                if curr == sq:
                    return level # cycle
                if curr < sq:
                    break
                que.append([curr - sq,level + 1])
        return curr_level