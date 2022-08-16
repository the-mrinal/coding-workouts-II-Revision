class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        cache = {}
        def dfs(index):
            nonlocal k
            if index == n:
                return 0
            
            if index not in cache:
                maxAns = float('-inf')
                currMax = float('-inf')
                currLen = 0
                for i in range(index ,min(n,index + k)):
                    currLen += 1
                    
                    currMax = max(currMax,arr[i])
                    
                    currSum = currMax*currLen + dfs(i + 1)

                    maxAns = max(currSum,maxAns)
                
                cache[index] = maxAns
            return cache[index]
        
        return dfs(0)