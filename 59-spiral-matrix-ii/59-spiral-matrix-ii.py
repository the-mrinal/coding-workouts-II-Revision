class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        startRow = 0
        startCol = 0
        limitRow = n
        limitCol = n
        count = 1
        while count <= (n*n):
            
            for col in range(startCol,limitCol):
                matrix[startRow][col] = count
                count += 1
            
            if count <= n*n:
                for row in range(startRow + 1,limitRow):
                    matrix[row][limitCol - 1] = count
                    count += 1
            if count <= n*n:
                for col in range(limitCol - 2,startCol-1,-1):
                    matrix[limitRow - 1][col] = count
                    count += 1
            if count <= n*n:
                for row in range(limitRow - 2,startRow,-1):
                    matrix[row][startCol] = count
                    count += 1
                    
            startRow += 1
            startCol += 1
            limitRow -= 1
            limitCol -= 1
            
        return matrix
    
    