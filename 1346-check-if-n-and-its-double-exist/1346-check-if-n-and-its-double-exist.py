class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        
        nums = set(arr)
        for num in nums:
            if num == 0:
                if freq[0] > 1:
                    return True
            elif num*2 in nums:
                return True
        
        return False
            