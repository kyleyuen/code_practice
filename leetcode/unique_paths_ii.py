class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]       
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]


s = Solution()
grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print s.uniquePathsWithObstacles(grid)