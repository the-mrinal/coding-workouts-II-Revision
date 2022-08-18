class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        adjMap = defaultdict(list)
        
        for a,b in redEdges: # 0 for red
            adjMap[a].append([b,0])
        for a,b in blueEdges:
            adjMap[a].append([b,1])
        
        que = deque()
        que.append([0,1,0])
        que.append([0,0,0])
        redAns = [0] + [float('inf')]*(n -1)
        blueAns = [0] + [float('inf')]*(n-1)
        visited = set()
        while que:
            curr,state,a = que.popleft()
            
            if state == 0:
                for b,S in adjMap[curr]:
                    if S == 1 and blueAns[b] > (a + 1):
                        blueAns[b] = a+1
                        que.append([b,S,a+1])
            else:
                for b,S in adjMap[curr]:
                    if S == 0 and redAns[b] > (a + 1):
                        redAns[b] = a + 1
                        que.append([b,S,a+1])
        ans = []
        for a,b in zip(redAns,blueAns):
            currAns = x if (x := min(a, b)) != float('inf') else -1
            ans.append(currAns)
        return ans