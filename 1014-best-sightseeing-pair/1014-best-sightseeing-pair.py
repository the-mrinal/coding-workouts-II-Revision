'''
val_i + val_j + (i - j)


'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        
        prevMax = 0
        maxSoFar = 0
        
        for i in range(len(values)):
            maxSoFar = max(maxSoFar,values[i] + prevMax)
            prevMax = max(values[i],prevMax) - 1
        
        return maxSoFar