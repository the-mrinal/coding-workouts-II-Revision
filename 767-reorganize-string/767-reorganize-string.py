class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxHeap = []
        for item,val in freq.items():
            heappush(maxHeap,[-val,item])
        
        
        prevC = 0
        prev = ""
        new_s = []
        # print(freq)
        while maxHeap:
            count,curr = heappop(maxHeap)
            new_s.append(curr)
            count += 1
            
            if prevC < 0:
                heappush(maxHeap,[prevC,prev])
            
            if count < 0:
                prevC = count
                prev = curr
            else:
                prevC = 0
                prev = ""
            
            
        return ''.join(new_s) if len(new_s) == len(s) else ""