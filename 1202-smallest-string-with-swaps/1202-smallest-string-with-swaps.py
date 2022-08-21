class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size - 1
    
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootB] > self.rank[rootA]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
    
    def isConnected(self,a,b):
        return self.find(a) == self.find(b)
    


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        
        uf = UnionFind(n)
        
        for a,b in pairs:
            uf.union(a,b)
        
        hashMap = defaultdict(list)
        
        for i in range(n):
            rootI = uf.find(i)
            hashMap[rootI].append([s[i],i])
        new_s = [0 for _ in range(n)]
        for R,values in hashMap.items():
            indexToUse = values.copy()
            sortedLetters = sorted(values)
            i = 0
            for _,index in indexToUse:
                new_s[index] = sortedLetters[i][0]
                i += 1
        return ''.join(new_s)
        
        
        
        
        
        
        
        