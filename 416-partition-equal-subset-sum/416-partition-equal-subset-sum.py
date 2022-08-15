class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        n = len(nums)

        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = True # True when target is empty.

        for t in range(target + 1):
            if nums[0] <= t:
                dp[0][t] = nums[0] == t

        for i in range(1,n):
            for j in range(1,target + 1):
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif nums[i] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i]]

        return dp[n-1][target]