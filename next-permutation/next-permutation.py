class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        def replace(index):
            prev = index + 1
            for i in range(n-1,index,-1):
                if nums[index] < nums[i]:
                    nums[i],nums[index] = nums[index],nums[i]
                    break
        
        for i in range(n-1,0,-1):
            if nums[i] > nums[i - 1]:
                replace(i-1)
                temp = i
                end = n - 1
                while temp < end:
                    nums[temp],nums[end] = nums[end],nums[temp]
                    temp += 1
                    end -= 1
                
                return
        nums.sort()
        