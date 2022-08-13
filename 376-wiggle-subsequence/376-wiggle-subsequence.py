class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [0] * n
        down = [0] * n
        
        for i in range(n):
            for j in range(0,i):
                if nums[i] < nums[j]:
                    down[i] = max(down[i],up[j] + 1)
                elif nums[i] > nums[j]:
                    up[i] = max(up[i],down[j] + 1)
        
        return 1 + max(up[n - 1],down[n - 1])