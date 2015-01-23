class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        row, column = 0, 0
        while row < m-1:
            if matrix[row][0] <= target < matrix[row+1][0]:
                break
            row += 1

        while column < n:
            if matrix[row][column] == target:
                return True
            column += 1

        return False


s = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

for i in range(51):
    if s.searchMatrix(matrix, i):
        print i