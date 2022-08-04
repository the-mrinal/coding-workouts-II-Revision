class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        indeg = {i:0 for i in range(numCourses)}
        
        for a,b in prerequisites:
            adjMap[b].append(a)
            indeg[a] += 1
        
        que = deque()
        
        for key,val in indeg.items():
            if val == 0:
                que.append(key)
        
        res = []
        
        while que:
            curr = que.popleft()
            
            res.append(curr)
            
            for ne in adjMap[curr]:
                indeg[ne] -= 1
                if indeg[ne] == 0:
                    que.append(ne)
        
        return res if len(res) == numCourses else []