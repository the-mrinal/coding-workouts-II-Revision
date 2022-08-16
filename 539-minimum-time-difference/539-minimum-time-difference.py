class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeArr = []
        
        def convert(time):
            return int(time[:2])*60 + int(time[3:])
        
        
        for time in timePoints:
            timeArr.append(convert(time))
        timeArr.sort()
        
        n = len(timeArr)

        minDiff = float('inf')
        # print()
        for x, y in zip(timeArr, timeArr[1:] + timeArr[:1]):
            minDiff = min(minDiff,(y - x)%(24*60))
        
        return minDiff
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            