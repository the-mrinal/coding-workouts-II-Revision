class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @lru_cache(None)
        def dfs(index,target):
            if target == 0:
                return True
            if index >= n:
                return False
            if target < 0:
                return False
            
            res = dfs(index + 1,target) or dfs(index + 1,target - nums[index])
            
            return res
        
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        return dfs(0,total // 2)