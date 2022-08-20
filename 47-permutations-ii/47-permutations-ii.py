class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        freq = Counter(nums)
        n = len(nums)
        def backtrack(comb,counter):
            if len(comb) == n:
                result.append(list(comb))
                return
            
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    comb.append(num)
                    backtrack(comb,counter)
                    comb.pop()
                    counter[num] += 1
        
        backtrack([],freq)
        return result