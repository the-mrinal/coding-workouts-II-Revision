class Solution:
    def longestCommonSubsequence(self, nums1: str, nums2: str) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        # dp[0][0] = 1 if nums1[0] == nums2[0] else 0
        maxVal = 0
        for i in range(1,n1 + 1):
            for j in range(1,n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j-1]
                else:
                    dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])
                maxVal = max(maxVal,dp[i][j])

        return maxVal
