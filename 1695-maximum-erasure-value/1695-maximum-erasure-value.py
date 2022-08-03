class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        numMap = {}
        currSum = 0
        maxSum = 0
        n = len(nums)
        start = 0
        for end in range(n):
            currSum += nums[end]
            
            if nums[end] in numMap:
                prev = start
                start = numMap[nums[end]] + 1
                while prev < start:
                    currSum -= nums[prev]
                    del numMap[nums[prev]]
                    prev += 1
            
            numMap[nums[end]] = end
            maxSum = max(maxSum,currSum)
            
        return maxSum