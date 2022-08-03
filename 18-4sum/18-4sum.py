class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def twoSum(nums,target):
            left = 0
            right = len(nums) - 1
            res = []
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left <= right:
                        left += 1
            return res
        
        def kSum(nums,target,k):
            if not nums:
                return []
            if k == 2:
                return twoSum(nums,target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for subsets in kSum(nums[i+1:],target - nums[i],k - 1):
                        res.append([nums[i]] + subsets)
            
            return res
        
        nums.sort()
        return kSum(nums,target,4)