class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # if even 2 possible roots
        # if ood only 1
        if n <= 2: return [i for i in range(n)]
        adjMap = {i:[] for i in range(n)}
        
        for a,b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        leaf = deque()
        for a,child in adjMap.items():
            if len(child) == 1:
                leaf.append(a)
        
        rem = n
        
        while rem > 2:
            rem -= len(leaf)
            new_leaf = deque()
            
            while leaf:
                curr = leaf.popleft()
                
                parent = adjMap[curr].pop()
                
                adjMap[parent].remove(curr)
                
                if len(adjMap[parent]) == 1:
                    new_leaf.append(parent)
            
            leaf = new_leaf
        
        return leaf
    