class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    print(i,left,right)
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
        
        return count