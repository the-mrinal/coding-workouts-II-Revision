class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        def findSum(index):
            nonlocal n
            left = index + 1
            right = n - 1
            localSum = float('inf')
            while left < right:
                currSum = nums[index] + nums[left] + nums[right]
                if abs(localSum - target) > abs(currSum - target):
                    localSum = currSum
                # print(localSum,currSum)
                if currSum - target < 0:
                    left += 1
                elif currSum - target > 0:
                    right -= 1
                else:
                    return currSum
            return localSum
        
        minSum = float('inf')
        for i in range(n):
            ans = findSum(i)
            if ans == target:
                return target
            else:
                if abs(target - minSum) > abs(target - ans):
                    minSum = ans
        
        return minSum