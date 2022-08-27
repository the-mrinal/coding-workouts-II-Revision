class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        new_arr = []
        
        for st,end in intervals:
            if toBeRemoved[0] < end:
                if toBeRemoved[1] <= st:
                    new_arr.append([st,end])    
                else:
                    if st < toBeRemoved[0]:
                        left = st
                        right = toBeRemoved[0]
                        new_arr.append([left,right])
                    if end > toBeRemoved[1]:
                        left = toBeRemoved[1]
                        right = end
                        new_arr.append([left,right])
            else:
                new_arr.append([st,end])
        return new_arr