class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return matrix
        n = len(matrix[0])
        
        # initialize state
        state = [[False for i in range(n+2)] for j in range(m+2)]
        for j in range(n+2):
            state[0][j] = True
            state[m+1][j] = True
        for i in range(m+2):
            state[i][0] = True
            state[i][n+1] = True

        result = []
        direction = 1
        row, column = 1, 1
        for i in range(m*n):
            state[row][column] = True
            result.append(matrix[row-1][column-1])
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
# array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array = [[], []]
print s.spiralOrder(array)