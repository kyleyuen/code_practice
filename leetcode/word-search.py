class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        row = len(board)
        if row == 0:
            return False
        column = len(board[0])
        
        for i in range(row):
            for j in range(column):
                if board[i][j] != word[0]:
                    continue

                state = [[True for m in range(column)] for n in range(row)]
                if self.search(board, state, i, j, word, 0):
                    return True

        return False


    def search(self, board, state, i, j, word, index):
        index += 1
        if len(word) == index:
            return True

        state[i][j] = False
        if (i > 0) and (state[i-1][j]) and (board[i-1][j] == word[index]):
            if self.search(board, state, i-1, j, word, index):
                return True
        if (j < len(board[0])-1) and (state[i][j+1]) and (board[i][j+1] == word[index]):
            if self.search(board, state, i, j+1, word, index):
                return True
        if (i < len(board)-1) and (state[i+1][j]) and (board[i+1][j] == word[index]):
            if self.search(board, state, i+1, j, word, index):
                return True
        if (j > 0) and (state[i][j-1]) and (board[i][j-1] == word[index]):
            if self.search(board, state, i, j-1, word, index):
                return True

        return False


s = Solution()
board = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"]
]

print s.exist([["a", "a"]], "aa")
print s.exist(board, "SEE")
print s.exist(board, "ABCCED")
print s.exist(board, "ABCB")