class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)



        dp_with0 = [0 for _ in range(n - 1)]
        dp_without0 = [0 for _ in range(n - 1)]

        dp_with0[0] = nums[0]
        dp_without0[0] = nums[1]

        dp_with0[1] = max(nums[:2])
        dp_without0[1] = max(nums[1:3])

        for i in range(2,n-1):
            dp_with0[i] = max(nums[i]+dp_with0[i - 2],dp_with0[i - 1])

        for i in range(3,n):
            dp_without0[i - 1] = max(nums[i] + dp_without0[i - 3], dp_without0[i - 2])

        return max(dp_without0[-1],dp_with0[-1])