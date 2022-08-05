class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        currSum = 0
        n = len(nums)
        count = 0
        for end in range(n):
            currSum += nums[end]
            
            while currSum*(end - start + 1) >= k and start <= end:
                currSum -= nums[start]
                start += 1
            
            if currSum * (end - start + 1) < k:
                count += (end - start + 1)
        
        return count