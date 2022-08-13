class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        cache = {}
        
        def findMaxWiggle(curr,prev,wasPos):
            if curr == n:
                return 1
            
            key = (curr,prev,wasPos)
            
            if key not in cache:
                ans1 , ans2 = 0,0
                if prev != curr and wasPos and nums[curr] < nums[prev]:
                    ans1 = 1 + findMaxWiggle(curr + 1,curr,False)
                elif prev != curr and not wasPos and nums[curr] > nums[prev]:
                    ans1 = 1 + findMaxWiggle(curr + 1,curr,True)

                ans2 = findMaxWiggle(curr + 1,prev,wasPos)
                
                cache[key] = max(ans1,ans2)
            
            return cache[key]
        
        findMaxWiggle(0,0,False)
        findMaxWiggle(0,0,True)        
        # print(cache)
        return max(cache[(0,0,True)],cache[(0,0,False)])