class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        limit = max(nums)
        
        points = [0] * (limit + 1)
        
        for num in nums:
            points[num] += num
        
        cache = {}
        def dp(index):
            if index == 0:
                return points[index]
            
            if index == 1:
                return max(points[:2])
            
            if index not in cache:
                cache[index] = 0
                
                ans1 = dp(index - 1)
                ans2 = dp(index - 2) + points[index]
                
                cache[index] = max(ans1,ans2)
            
            return cache[index]
        
        return dp(limit)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        