class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxVal = 0
        
        while left < right:
            currC = (right - left)*min(height[left],height[right])
            maxVal = max(currC,maxVal)
            print(left,right)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxVal