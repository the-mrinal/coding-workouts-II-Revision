class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def findNeighbours(curr):
            neigh = []
            for i in range(4):
                temp = int(curr[i])
                for d in (-1,1):
                    n_d = (temp + d)%10
                    neigh.append(curr[:i]+str(n_d)+curr[i+1:])
            return neigh
        que = deque()
        que.append(["0000",0])
        visited = set()
        visited.add("0000")
        
        while que:
            curr,level = que.popleft()
            
            if curr == target:
                return level
            if curr in deadends:
                continue
            
            for neigh in findNeighbours(curr):
                if neigh not in visited:
                    visited.add(neigh)
                    que.append([neigh,level + 1])
        
        return -1