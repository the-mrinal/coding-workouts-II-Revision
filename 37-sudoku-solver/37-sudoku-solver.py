class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i,j,number):
            return not(number in self.row[i] or number in self.col[j] or number in self.box[findBoxInd(i,j)])
        
        def pick_number(i,j,number):
            self.row[i][number] += 1
            self.col[j][number] += 1
            self.box[findBoxInd(i,j)][number] += 1
            board[i][j] = str(number)
        
        def remove_number(i,j,number):
            del self.row[i][number]
            del self.col[j][number]
            del self.box[findBoxInd(i,j)][number]
            board[i][j] = "."
        
        def pick_next_number(i,j):
            nonlocal sudoku_solved,N
            if i == N - 1 and j == N - 1:
                sudoku_solved = True
            else:
                if j == N -1:
                    backtrack(i + 1,0)
                else:
                    backtrack(i,j + 1)
        
        def backtrack(row,col):
            nonlocal sudoku_solved
            if board[row][col] == '.':
                for num in range(1,10):
                    if isValid(row,col,num):
                        pick_number(row,col,num)
                        pick_next_number(row,col)
                        if not sudoku_solved:
                            remove_number(row,col,num)
            else:
                pick_next_number(row,col)
        
        
        n = 3
        
        N = 3*3
        
        findBoxInd = lambda row,col: (row//n)*n + col // n
        
        self.row = [defaultdict(int) for _ in range(N)]
        self.col = [defaultdict(int) for _ in range(N)]        
        self.box = [defaultdict(int) for _ in range(N)]        
        
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    pick_number(i,j,int(board[i][j]))
        
        sudoku_solved  = False
        
        backtrack(0,0)