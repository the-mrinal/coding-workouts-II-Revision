class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def findZeros(index):
            left = index + 1
            right = n - 1
            
            while left < right:
                target = nums[index] + nums[left] + nums[right]
                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                else:
                    res.append([nums[index],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            findZeros(i)
        return res