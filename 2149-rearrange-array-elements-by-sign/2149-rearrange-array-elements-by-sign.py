class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        poStack = deque()
        negStack = deque()
        
        for i in range(n):
            if nums[i] > 0:
                poStack.append(nums[i])
            else:
                negStack.append(nums[i])
        
        for i in range(n//2):
            result.append(poStack.popleft())
            result.append(negStack.popleft())
        
        return result