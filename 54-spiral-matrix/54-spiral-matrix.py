class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        startRow = 0
        startCol = 0
        limitRow = m
        limitCol = n
        res = []
        count = 0
        while count < (m*n):
            
            for col in range(startCol,limitCol):
                res.append(matrix[startRow][col])
                count += 1

            if count < (m*n):
                for row in range(startRow + 1,limitRow):
                    res.append(matrix[row][limitCol - 1])
                    count += 1

            if count < (m*n):
                for col in range(limitCol - 2,startCol - 1,-1):
                    res.append(matrix[limitRow - 1][col])
                    count += 1

            if count < (m*n):
                for row in range(limitRow - 2,startRow,-1):
                    res.append(matrix[row][startCol])
                    count += 1

            
            startCol += 1
            startRow += 1
            limitRow -= 1
            limitCol -= 1
        
        return res