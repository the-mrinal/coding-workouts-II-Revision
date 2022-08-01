class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for index,num in enumerate(mat):
            res.append([sum(num),index])
        
        res.sort()
        ans = []
        for i in range(k):
            ans.append(res[i][1])
        
        return ans