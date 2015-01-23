class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if (len(s)==0) or (s[0]=="0"):
            return 0
        
        dp = [0 for i in range(len(s)+1)]
        dp[0] = dp[1] = 1
        for i in range(2, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]


s = Solution()
print s.numDecodings("01")