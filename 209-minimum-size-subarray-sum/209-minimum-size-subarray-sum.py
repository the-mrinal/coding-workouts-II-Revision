class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        currSum = 0
        minLength = float('inf')
        n = len(nums)
        for end in range(n):
            currSum += nums[end]
            
            while currSum >= target and start < end:
                currSum -= nums[start]
                start += 1
            if currSum < target and start > 0:
                currSum += nums[start-1]
                start -= 1
            
            if currSum >= target:
                minLength = min(minLength,end - start + 1)
        
        return minLength if minLength < float('inf') else 0