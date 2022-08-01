class UnionFind:
    
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.count = size
        
    
    def find(self,x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def insert(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
            self.count -= 1
    
    def isConnected(self,a,b):
        return self.find(a) == self.find(b)
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        for a,b in connections:
            uf.insert(a,b)
        
        minEdgeReq = n - 1
        currEdgeRemaining = uf.count
        
        availEdge = len(connections)
        
        if minEdgeReq > availEdge:
            return -1
        
        return currEdgeRemaining - 1
        