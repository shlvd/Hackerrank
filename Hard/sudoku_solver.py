def solveSudoku(board):
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                    
                for c in "123456789":
                    if isValid(board, i, j, c):
                        board[i][j] = c        
                        if solveSudoku(board):
                            return True
                        board[i][j] = '.'
                return False
        return True
                        
def isValid(board, row, col, c):
    for i in range(9):
        if board[i][col] == c or board[row][i] == c or\
            board[row//3*3+i//3][col//3*3+i%3] == c:
            return False
    return True
