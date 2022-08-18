class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts = [0] + horizontalCuts + [h]
        
        verticalCuts = [0] + verticalCuts + [w]
        
        maxHeight = float('-inf')
        
        maxWidth = float('-inf')
        
        for i in range(1,len(horizontalCuts)):
            maxHeight = max(maxHeight,horizontalCuts[i] - horizontalCuts[i - 1])
        
        for i in range(1,len(verticalCuts)):
            maxWidth = max(maxWidth,verticalCuts[i] - verticalCuts[i - 1])
        
        # print(maxHeight,maxWidth)
        return (maxHeight*maxWidth)%(10**9 + 7)