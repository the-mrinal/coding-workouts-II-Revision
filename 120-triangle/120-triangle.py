class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev = triangle[-1]
        curr = [0]*(n-1)
        
        for level in range(n - 2, -1, -1):
            for i in range(level + 1):
                curr[i] = triangle[level][i]+min(prev[i],prev[i+1])
            
            curr,prev = [0]*level,curr
        return prev[0]
        