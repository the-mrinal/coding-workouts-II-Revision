class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        
        adjMap = defaultdict(list)
        n = len(edges)
        
        for a,b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
            
        que = deque()
        
        que.append([0,0])
        
        seen = set()
        short = [float('inf') for i in range(n + 1)]
        
        while que:
            curr,dist = que.popleft()
            
            if curr in seen:
                continue
            
            seen.add(curr)
            short[curr] = dist
            
            for b in adjMap[curr]:
                if b not in seen:
                    que.append([b,dist + 1])
        
        res = []
        for dist,pat in zip(short,patience):
            if pat > 0:
                num = (dist * 2) + (((dist * 2) - 1)//pat)*pat
                res.append(num)
        
        return max(res) + 1