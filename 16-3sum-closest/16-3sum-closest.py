class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        for  i in range(len(nums) - 2):
            j , k = i + 1,len(nums) - 1
            
            while j < k:
                
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == target:
                    return currSum
                if abs(currSum - target) < abs(result - target):
                    result = currSum
                
                if currSum < target:
                    j += 1
                elif currSum > target:
                    k -= 1
        
        return result