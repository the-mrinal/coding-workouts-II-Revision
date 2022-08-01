class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        
        while numRows > 2:
            res.append([])
            res[-1].append(1)
            for i in range(len(res[-2]) - 1):
                res[-1].append(res[-2][i] + res[-2][i+1])
            res[-1].append(1)
            numRows -= 1
        
        return res if numRows > 1 else [[1]]
        