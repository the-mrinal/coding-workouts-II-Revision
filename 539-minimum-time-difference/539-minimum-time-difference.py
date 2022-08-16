class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        
        def convertTime(t):
            return (int(t[:2])*60 + int(t[3:]))
        
        for t in timePoints:
            time.append(convertTime(t))
        time.sort()
        mindiff = 999999
        for x,y in zip(time,time[1:]+time[:1]): # for handling cirluar ie,first will come after last
            diff = (y - x)%(24*60)
            mindiff = min(diff,mindiff)
        return mindiff
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            