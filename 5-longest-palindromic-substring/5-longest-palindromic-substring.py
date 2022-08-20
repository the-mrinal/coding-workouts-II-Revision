class Solution:
    def longestPalindrome(self, nums: str) -> str:
        n = len(nums)
        maxCount = 0
        maxVal = ""
        def findP(left,right):
            nonlocal maxCount,maxVal
            count = 0
            while left >= 0 and right < n and nums[left] == nums[right]:
                if left == right:
                    count += 1
                else:
                    count += 2
                left -= 1
                right += 1
            if maxCount < count:
                maxCount = count
                maxVal = nums[left + 1:right]
        
        for i in range(n):
            findP(i,i)
            findP(i,i + 1)
        
        return maxVal