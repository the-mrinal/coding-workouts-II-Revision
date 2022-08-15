class Solution:
    
    def helper(self,nums,target,index,curr_sum,cache):
        if (index,curr_sum) in cache:
            return cache[(index,curr_sum)]
        
        if index < 0 and target == curr_sum:
            return 1
        elif index < 0:
            return 0
        
        
        
        countN = self.helper(nums,target,index - 1,curr_sum - nums[index],cache)
        
        countP = self.helper(nums,target,index - 1,curr_sum + nums[index],cache)
        
        cache[(index,curr_sum)] = countN + countP
        
        return cache[(index,curr_sum)]
    
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        curr_sum = 0
        index = len(nums) - 1
        return self.helper(nums,target,index,curr_sum,cache)