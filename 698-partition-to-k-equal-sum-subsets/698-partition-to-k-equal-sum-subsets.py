class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        
        n = len(nums)
        
        if total % k != 0:
            return False
        
        target = total // k
        
        taken = ['0'] * n
        
        nums.sort(reverse=True)
        cache = {}
        def backtrack(index,count,currSum):
            nonlocal n
            if count == k - 1:
                return True # total is divisible by k
            
            if currSum > target:
                return False
            
            key = ''.join(taken)
            
            if key not in cache:
                if currSum == target:
                    cache[key] = backtrack(0,count + 1,0)
                    return cache[key]

                for i in range(index,n):
                    if not taken[i] == '1':
                        taken[i] = '1'

                        if backtrack(i + 1,count,currSum + nums[i]):
                            cache[key] = True
                            return True

                        taken[i] = '0'
            cache[key] = False
            return cache[key]
        
        return backtrack(0,0,0)