class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            if not self.check_row(board, i):
                return False

        for j in range(9):
            if not self.check_column(board, j):
                return False

        for i in range(3):
            for j in range(3):
                if not self.check_square(board, i, j):
                    return False

        return True


    def check_row(self, board, row):
        state = [False for i in range(9+1)]
        for j in range(9):
            if board[row][j] == ".":
                continue
            else:
                digit = int(board[row][j])
                if state[digit]:
                    return False
                state[digit] = True
        return True


    def check_column(self, board, column):
        state = [False for i in range(9+1)]
        for i in range(9):
            if board[i][column] == ".":
                continue
            else:
                digit = int(board[i][column])
                if state[digit]:
                    return False
                state[digit] = True
        return True


    def check_square(self, board, row, column):
        state = [False for i in range(9+1)]
        for i in range(3):
            for j in range(3):
                if board[row*3+i][column*3+j] == ".":
                    continue
                else:
                    digit = int(board[row*3+i][column*3+j])
                    if state[digit]:
                        return False
                    state[digit] = True
        return True


s = Solution()
board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print s.isValidSudoku(board)