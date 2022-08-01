class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for num in nums:
            numset.add(num)
        
        
        maxSoFar = 0
        for num in numset:
            if num - 1 not in numset:
                curr = 0
                temp = num
                while temp in numset:
                    curr += 1
                    temp += 1
                maxSoFar = max(maxSoFar,curr)
        
        return maxSoFar