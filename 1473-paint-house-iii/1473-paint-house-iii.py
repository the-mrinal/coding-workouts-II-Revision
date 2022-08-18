class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        cache = {}
        
        def dfs(index,neigh,color):
            key = (index,neigh,color)
            
            if index == m or neigh < 0 or m - index < neigh:
                return 0 if index == m and neigh == 0 else float('inf')
            
            if key not in cache:
                if houses[index] == 0:
                    cache[key] = min(dfs(index + 1,neigh - (n_color != color),n_color) + cost[index][n_color - 1] for n_color in range(1,n + 1))
                else:
                    cache[key] = dfs(index + 1,neigh-(houses[index] != color),houses[index])
            
            return cache[key]
        
        dfs(0,target,-1)
        return cache[(0,target,-1)] if cache[(0,target,-1)] < float('inf') else -1