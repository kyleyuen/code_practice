class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n/2):
            self.rotate_edge(matrix, i, n)
        return matrix


    def rotate_edge(self, matrix, offset, n):
        for i in range(offset, n-1-offset):
            a, b = matrix[offset][i], matrix[i][n-1-offset]
            c, d = matrix[n-1-offset][n-1-i], matrix[n-1-i][offset]
            matrix[offset][i] = d
            matrix[i][n-1-offset] = a
            matrix[n-1-offset][n-1-i] = b
            matrix[n-1-i][offset] = c
        return matrix


s = Solution()
array = []
n = 5
for i in range(n):
    line = []
    for j in range(n):
        line.append(i*n+j+1)
    array.append(line)
print s.rotate(array)