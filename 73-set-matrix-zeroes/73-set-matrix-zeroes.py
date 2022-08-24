class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        def resetRowCol(i,j):
            for col in range(n):
                matrix[i][col] = 0
            for row in range(m):
                matrix[row][j] = 0

        zeros = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.add((i,j))
        
        for x,y in zeros:
            resetRowCol(x,y)