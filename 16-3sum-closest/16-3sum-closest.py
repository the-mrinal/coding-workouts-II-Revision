class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                
                if currSum == target:
                    return target
                
                if abs(currSum - target) < abs(res - target):
                    res = currSum
                
                if currSum < target:
                    left += 1
                elif currSum > target:
                    right -= 1
            
        return res
    

#     class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         result = float('inf')
#         for  i in range(len(nums) - 2):
#             j , k = i + 1,len(nums) - 1
            
#             while j < k:
                
#                 currSum = nums[i] + nums[j] + nums[k]
#                 if currSum == target:
#                     return currSum
#                 if abs(currSum - target) < abs(result - target):
#                     result = currSum
                
#                 if currSum < target:
#                     j += 1
#                 elif currSum > target:
#                     k -= 1
        
#         return result