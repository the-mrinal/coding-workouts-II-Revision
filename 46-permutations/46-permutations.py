class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def allpermutations(index):
            if index == n - 1:
                return [[nums[index]]]
            
            ans = allpermutations(index + 1)
            
            new_ans = []
            
            for i in range(len(ans)):
                for j in range(len(ans[i]) + 1):
                    curr = ans[i][:j]+[nums[index]] + ans[i][j:]
                    new_ans.append(curr)
            
            return new_ans
        return allpermutations(0)
    