class UnionFind:
    
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size - 1
        self.timeA = []
    
    def find(self,x):
        if self.root[x] == x:
            return self.root[x]
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,a,b,time):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            heappush(self.timeA,-time)
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
            
            self.count -= 1
                
    
    

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)
        for time,a,b in logs:
            uf.union(a,b,time)
        if uf.count != 0:
            return -1
        
        
        
        return -uf.timeA[0]
        