class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = (nums[n//2] + nums[n//2 - 1])//2 if n % 2 == 0 else nums[n//2]
        count = 0
        for num in nums:
            count += abs(num - median)
            
        return count