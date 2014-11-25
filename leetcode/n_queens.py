class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        result = []
        board = [[False for i in range(n)] for j in range(n)]
        self.dfs(board, 0, n, result)
        return result


    def dfs(self, board, column, n, result):
        if column == n:
            result.append(self.board_to_string(board, n))
            return

        for i in range(n):
            board[i][column] = True
            if not self.is_conflict(board, i, column, n):
                self.dfs(board, column+1, n, result)
            board[i][column] = False


    def is_conflict(self, board, row, column, n):
        # check row
        for i in range(column):
            if board[row][i]:
                return True

        # check diagonal
        for i in range(1, min(row, column)+1):
            if board[row-i][column-i]:
                return True

        # check counter-diagonal
        for i in range(1, min(n-row, column+1)):
            if board[row+i][column-i]:
                return True

        return False


    def board_to_string(self, board, n):
        result = []
        for i in range(n):
            line = ""
            for j in range(n):
                if board[i][j]:
                    line += "Q"
                else:
                    line += "."
            result.append(line)
        return result


s = Solution()
print len(s.solveNQueens(8))