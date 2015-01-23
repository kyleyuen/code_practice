class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        state = [[True for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    state[i][j] = False

        (x, y) = self.next_blank(state, 0, -1)
        self.dfs(board, x, y, state)
        print board


    def dfs(self, board, row, column, state):
        if row == -1 and column == -1:
            return True

        (x, y) = self.next_blank(state, row, column)
        digits = [str(i) for i in range(1, 10)]
        for d in digits:
            if self.check_row(board, row, d) and self.check_column(board, column, d) \
                and self.check_square(board, int(row/3), int(column/3), d):
                board[row][column] = d
                if self.dfs(board, x, y, state):
                    return True
                board[row][column] = "."
        return False


    def check_row(self, board, row, value):
        for j in range(9):
            if board[row][j] == value:
                return False
        return True


    def check_column(self, board, column, value):
        for i in range(9):
            if board[i][column] == value:
                return False
        return True


    def check_square(self, board, row, column, value):
        for i in range(3):
            for j in range(3):
                if board[row*3+i][column*3+j] == value:
                    return False
        return True


    def next_blank(self, state, row, column):
        for j in range(column+1, 9):
            if state[row][j]:
                return (row, j)

        for i in range(row+1, 9):
            for j in range(9):
                if state[i][j]:
                    return (i, j)
        return (-1, -1)
        

s = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
]
board = [".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]
processed_board = []
for i in range(len(board)):
    temp = []
    for c in board[i]:
        temp.append(c)
    processed_board.append(temp)
s.solveSudoku(processed_board)