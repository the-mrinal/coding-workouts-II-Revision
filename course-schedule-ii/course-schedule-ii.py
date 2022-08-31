class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        indeg = [0]*numCourses
        
        for a,b in prereq:
            adjMap[b].append(a)
            indeg[a] += 1
        
        que = deque()
        for index in range(numCourses):
            if indeg[index] == 0:
                que.append(index)
        
        res = []
        print(que)
        while que:
            curr = que.popleft()
            
            res.append(curr)
            
            for ch in adjMap[curr]:
                indeg[ch] -= 1
                if indeg[ch] == 0:
                    que.append(ch)
        
        return res if len(res) == numCourses else []