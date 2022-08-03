class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = currMax
        maxSoFar = currMax
        
        for i in range(1,len(nums)):
            temp = max(nums[i],currMax*nums[i],currMin*nums[i])
            currMin = min(nums[i],currMin*nums[i],currMax*nums[i])
            currMax = temp
            maxSoFar = max(currMax,maxSoFar)
        
        return maxSoFar