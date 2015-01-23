class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        result = [[0 for i in range(n)] for j in range(n)]
        
        # initialize state
        state = [[False for i in range(n+2)] for j in range(n+2)]
        for j in range(n+2):
            state[0][j] = True
            state[n+1][j] = True
        for i in range(n+2):
            state[i][0] = True
            state[i][n+1] = True

        direction = 1
        row, column = 1, 1
        for i in range(n*n):
            state[row][column] = True
            result[row-1][column-1] = i+1
            if direction == 0:
                if state[row-1][column]:
                    column += 1
                    direction = 1
                else:
                    row -= 1
            elif direction == 1:
                if state[row][column+1]:
                    row += 1
                    direction = 2
                else:
                    column += 1
            elif direction == 2:
                if state[row+1][column]:
                    column -= 1
                    direction = 3
                else:
                    row += 1
            elif direction == 3:
                if state[row][column-1]:
                    row -= 1
                    direction = 0
                else:
                    column -= 1
        return result


s = Solution()
print s.generateMatrix(2)
print s.generateMatrix(3)