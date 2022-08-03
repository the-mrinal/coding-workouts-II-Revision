class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        index = 1
        while count < k:
            if index not in arr:
                count += 1
            index += 1
        
        return index - 1