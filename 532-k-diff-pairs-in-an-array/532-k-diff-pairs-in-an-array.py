class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 1
        n = len(nums)
        
        
        count = 0
        
        while left < n and right < n:
            target = nums[right] - nums[left]
            
            if target < k or left == right:
                right += 1
            elif target > k:
                left += 1
            else:
                left += 1
                count += 1
                while left < n and nums[left] == nums[left - 1]:
                    left += 1
        return count