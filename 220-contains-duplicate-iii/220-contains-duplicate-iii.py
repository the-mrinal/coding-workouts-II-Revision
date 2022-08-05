class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # bucket sort
        n = len(nums)
        buckets = {}
        
        
        for i in range(n):
            index = nums[i] // (t+1)
            
            if index in buckets:
                return True # find same num hence no need to check diff.
            
            if index - 1 in buckets and abs(nums[i] - buckets[index - 1]) <= t:
                return True
            if index + 1 in buckets and abs(nums[i] - buckets[index + 1]) <= t:
                return True
            
            buckets[index] = nums[i]
            
            if i >= k:
                del buckets[(nums[i - k] // (t+1))]
        
        
