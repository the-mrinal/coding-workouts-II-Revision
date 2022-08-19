class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1 for _ in range(2)] for _ in range(n)]
        
        maxVal = 1
        
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] >= dp[i][0]:
                        dp[i][0] = 1 + dp[j][0]
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] = dp[i][1] + dp[j][1]
                maxVal = max(dp[i][0],maxVal)

        count = 0
        for i in dp:
            if i[0] == maxVal:
                count += i[1] 
        return count