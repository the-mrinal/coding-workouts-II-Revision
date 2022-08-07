class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        def findSum(index):
            nonlocal n
            left = index + 1
            right = n- 1
            while left < right:
                currSum = nums[index] + nums[left] + nums[right]
                
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    ans.append([nums[index],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            
        
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                findSum(i)
        
        return ans