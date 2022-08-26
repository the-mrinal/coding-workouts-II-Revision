class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        rangeMap = defaultdict(int)
        
        for start,end,inc in updates:
            rangeMap[start] += inc
            rangeMap[end + 1] -= inc
        
        res = [0]*length
        currVal = 0
        
        for index in range(length):
            if index in rangeMap:
                currVal += rangeMap[index]
            res[index] = currVal
        
        return res