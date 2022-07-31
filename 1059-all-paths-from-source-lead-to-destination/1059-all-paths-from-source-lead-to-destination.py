class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        adjMap  = defaultdict(list)
        
        for a,b in edges:
            adjMap[a].append(b)
        
        stack = [[source,[source]]]
        while stack:
            curr,path = stack.pop()
            if curr not in adjMap:
                if curr == dest:
                    continue
                else:
                    return False
            for b in adjMap[curr]:
                if b in path:
                    return False
                else:
                    stack.append([b,path + [b]])
                
            
        return True