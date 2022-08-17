class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        maxHeap = []
        
        freq = Counter(s)
        
        for item,count in freq.items():
            heappush(maxHeap,[-count,item])
            
        que = deque()
        
        ans = []
        
        while maxHeap:
            curr_count,curr = heappop(maxHeap)
            
            ans.append(curr)
            
            que.append([curr_count + 1,curr])
            
            if len(que) >= k:
                count,item = que.popleft()
                if -count > 0:
                    heappush(maxHeap,[count,item])
        
        return ''.join(ans) if len(ans) == len(s) else ""