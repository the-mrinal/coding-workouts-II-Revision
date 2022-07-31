class Solution:
    def maxArea(self, nums: List[int]) -> int:
        '''
        [1,2,3,4,5,7]
        
        a
        b
        maximise - diff(a,b)*min(a,b)
        
        heap with maxHeap forumula abs(a_index - b_index)
        
        
        '''
        left = 0
        right = len(nums) - 1
        maxSum = -1
        while left < right:
            maxSum = max(maxSum,min(nums[left],nums[right])*(right - left))
            
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
                
        
        return maxSum