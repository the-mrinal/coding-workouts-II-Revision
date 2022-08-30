class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        right = [0]
        n = len(height)
        
        for i in range(1,n):
            left.append(max(left[-1],height[i - 1]))
            right.append(max(right[-1],height[n - i]))
        
        waterLog = 0
        
        for i in range(n):
            currLog = max(0,min(left[i],right[n - i-1]) - height[i])
            waterLog += currLog
        return waterLog