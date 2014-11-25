class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        state = [[True for i in range(9)] for j in range(9)]
        processed_board = self.translate_board_from_string_to_integet(board, state)

        finished = False
        self.dfs(processed_board, 0, 0, state, finished)

        return self.translate_board_from_integer_to_string(processed_board)


    def translate_board_from_string_to_integet(self, board, state):
        processed_board = [[0 for i in range(9)] for j in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    processed_board[i][j] = int(board[i][j])
                    state[i][j] = False
        return processed_board


    def translate_board_from_integer_to_string(self, processed_board):
        board = []
        for i in range(len(processed_board)):
            row = ""
            for j in range(len(processed_board[i])):
                if processed_board[i][j] == 0:
                    row += "."
                else:
                    row += str(processed_board[i][j])
            board.append(row)
        return board


    def dfs(self, processed_board, row, column, state, finished):
        if finished:
            return

        (x, y) = self.next_blank(state, row, column)
        if x == -1 and y == -1:
            finished = True
            return

        for i in range(1, 10):
            processed_board[x][y] = i
            if self.check_row(processed_board, row) \
            and self.check_column(processed_board, column) \
            and self.check_square(processed_board, int(row/3), int(column/3)):
                self.dfs(processed_board, x, y, state, finished)
        state[x][y] = False


    def check_row(self, processed_board, row):
        state = [False for i in range(9+1)]
        for j in range(9):
            if processed_board[row][j] == 0:
                continue

            if state[processed_board[row][j]]:
                return False
            state[processed_board[row][j]] = True
        return True


    def check_column(self, processed_board, column):
        state = [False for i in range(9+1)]
        for i in range(9):
            if processed_board[i][column] == 0:
                continue

            if state[processed_board[i][column]]:
                return False
            state[processed_board[i][column]] = True
        return True


    def check_square(self, processed_board, row, column):
        state = [False for i in range(9+1)]
        for i in range(3):
            for j in range(3):
                if processed_board[row*3+i][column*3+j] == 0:
                    continue

                if state[processed_board[row*3+i][column*3+j]]:
                    state[processed_board[row*3+i][column*3+j]] = True
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
board = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
print s.solveSudoku(board)