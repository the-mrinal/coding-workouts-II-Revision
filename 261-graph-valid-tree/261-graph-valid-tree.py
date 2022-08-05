class UnionFind:
    
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.count = size - 1
    
    def find(self,x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootA] = rootB
            elif self.rank[rootB] > self.rank[rootA]:
                self.root[rootB] = rootA
            else:
                self.root[rootA] = rootB
                self.rank[rootA] += 1
            self.count -= 1
            return True
        else:
            return False
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        
        for a,b in edges:
            if not uf.union(a,b):
                return False
        return True if uf.count == 0 else False 