class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            dp[i][1] = 1
        for j in range(n+1):
            dp[1][j] = 1

        for i in range(2, m+1):
            for j in range(2, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]


s = Solution()
print s.uniquePaths(4, 8)