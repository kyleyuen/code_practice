class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        left = [0 for i in range(n)]
        right = [n for i in range(n)]
        height = [0 for i in range(n)]
        
        result = 0
        for i in range(m):
            # calculate height
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0

            # calculate left
            current_left = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], current_left)
                else:
                    left[j] = 0
                    current_left = j+1

            # calculate right
            current_right = n
            for j in reversed(range(n)):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], current_right)
                else:
                    right[j] = n
                    current_right = j

            # calculate area
            for j in range(n):
                area = (right[j] - left[j]) * height[j]
                if result < area:
                    result = area
        return result


s = Solution()
matrix = [
    ["1", "1"],
    ["1", "0"],
]
print s.maximalRectangle(matrix)