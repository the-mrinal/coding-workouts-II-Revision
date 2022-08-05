class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        n = len(nums)
        for i in range(1,n):
            ans.append(ans[-1]*nums[i-1])
        
        right = 1
        for i in range(n-2,-1,-1):
            temp = right * nums[i +1]
            ans[i] = ans[i] * temp
            right = temp
        
        return ans