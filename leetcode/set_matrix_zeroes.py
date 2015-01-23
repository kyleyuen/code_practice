class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        if m == 0:
            return matrix
        n = len(matrix[0])

        need_to_set = 1e6
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = need_to_set

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == need_to_set:
                    matrix[i][j] = 0
                    for x in range(m):
                        if matrix[x][j] != need_to_set:
                            matrix[x][j] = 0
                    for y in range(n):
                        if matrix[i][y] != need_to_set:
                            matrix[i][y] = 0
        return matrix
                    
s = Solution()
matrix = [[0, 2, 3], [4, 0, 6], [7, 8, 9]]
print s.setZeroes(matrix)