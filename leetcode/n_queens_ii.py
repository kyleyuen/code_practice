class Solution:
    # @return an integer
    def totalNQueens(self, n):
        result = [0]
        board = [[False for i in range(n)] for j in range(n)]
        self.dfs(board, 0, n, result)
        return result[0]


    def dfs(self, board, column, n, result):
        if column == n:
            result[0] += 1
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


s = Solution()
print s.totalNQueens(8)