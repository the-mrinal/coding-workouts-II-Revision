class Solution:
    def nextClosestTime(self, time: str) -> str:
        nums = []
        for t in time:
            if t != ":":
                nums.append(t)
        
        minute = time[3:]
        hour = time[:2]
    
        totalPossibleItems = [a+b for a in nums for b in nums]
        totalPossibleItems = set(totalPossibleItems)
        totalPossibleItems = list(totalPossibleItems)
        totalPossibleItems.sort()
        index_min = totalPossibleItems.index(minute)
        n = len(totalPossibleItems)
        if index_min + 1 < n and totalPossibleItems[index_min + 1] < "60":
            return hour +":"+totalPossibleItems[index_min + 1]
        
        index_hr = totalPossibleItems.index(hour)
        
        if index_hr + 1 < n and totalPossibleItems[index_hr + 1]  < "24":
            return totalPossibleItems[index_hr + 1]+":"+totalPossibleItems[0]
        
        return totalPossibleItems[0] +":" + totalPossibleItems[0]        
        
        