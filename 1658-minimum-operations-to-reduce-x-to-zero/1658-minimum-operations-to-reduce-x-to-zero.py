class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # longest subarr that sums up to sum(nums) -x
        
        target = sum(nums) - x
        currMax = 0
        maxSoFar = -1
        start = 0
        for end in range(len(nums)):
            currMax += nums[end]
            
            while currMax > target and start <= end:
                currMax -= nums[start]
                start += 1
                
            if currMax == target:
                maxSoFar = max(maxSoFar,end - start + 1)
        
        return len(nums) - maxSoFar  if maxSoFar != -1 else -1
        