class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {}
        
        def dfs(index,currSum):
            if currSum == 0 and index == n:
                return 1
            
            if index >= n:
                return 0
            
            key = (index,currSum)
            
            if key not in cache:
                sum1 = dfs(index + 1,currSum + nums[index])
                sum2 = dfs(index + 1,currSum - nums[index])
                cache[key] = sum1 + sum2
            
            return cache[key]
        
        return dfs(0,target)