class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]


s = Solution()
for i in range(10):
    print s.climbStairs(i)