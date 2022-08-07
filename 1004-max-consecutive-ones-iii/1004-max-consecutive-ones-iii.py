class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        for end in range(n):
            k -= 1 - nums[end]
            
            if k < 0:
                k += 1 - nums[left]
                left += 1
      
        return end - left + 1