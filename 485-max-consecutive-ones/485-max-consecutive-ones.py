class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSoFar = 0
        currSum = 0
        for num in nums:
            currSum += num
            if num == 0:
                maxSoFar = max(currSum,maxSoFar)
                currSum = 0
        maxSoFar = max(currSum,maxSoFar)                
        return maxSoFar