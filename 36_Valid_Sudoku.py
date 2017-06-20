def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for i in range(9):
        row = {}
        column = {}
        cube = {}
        for j in range(9):
            cube_i = (j / 3) + 3 * (i / 3)
            cube_j = j % 3 + 3 * (i % 3)
            if board[i][j] != '.' and board[i][j] in row:
                return False
            elif board[i][j] != '.':
                row[board[i][j]] = True
            if board[j][i] != '.' and board[j][i] in column:
                return False
            elif board[j][i] != '.':
                column[board[j][i]] = True
            if board[cube_i][cube_j] != '.' and board[cube_i][cube_j] in cube:
                return False
            elif board[cube_i][cube_j] != '.':
                cube[board[cube_i][cube_j]] = True
    return True

def isValidSudoku2(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = int(board[i][j]) - 1
                k = i / 3 * 3 + j / 3
                print num, k


test = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
# isValidSudoku(test)
isValidSudoku2(test)