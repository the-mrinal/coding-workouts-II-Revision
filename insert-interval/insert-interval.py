class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        new_arr = []
        isInserted = False
        for st,end in intervals:
            left = newInterval[0] if not isInserted else new_arr[-1][0]
            right = newInterval[1] if not isInserted else new_arr[-1][1]
            if end >= left:
                if not(st > right):
                    n_left = min(left,st)
                    n_right = max(right,end)
                    if (n_left,n_right) not in new_arr:
                        if isInserted:
                            new_arr.pop()
                        new_arr.append((n_left,n_right))
                    if isInserted == False:
                        isInserted = True
                else:
                    if not isInserted:
                        new_arr.append((left,right))
                        isInserted = True
                    new_arr.append((st,end))
            else:
                new_arr.append((st,end))
        if not isInserted:
            new_arr.append(newInterval)
        
        return new_arr