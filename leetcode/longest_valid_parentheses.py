class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        dp = [0 for i in range(len(s))]

        for i in range(1, len(s)):
            if s[i] == ")":
                if (s[i-1]=="("):
                    if i == 1:
                        dp[i] = 2
                    else :
                        dp[i] = dp[i-2] + 2
                elif s[i-1]==")" and (i-dp[i-1]-1>=0) and s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2

        result = 0
        for i in range(len(s)):
            if result < dp[i]:
                result = dp[i]
        return result


    # @param s, a string
    # @return an integer
    # def longestValidParentheses(self, s):
    #     stack = []

    #     for i in range(len(s)):
    #         if s[i] == "(":
    #             stack.append(i)
    #         elif s[i] == ")":
    #             if len(stack) == 0:
    #                 stack.append(i)
    #             else:
    #                 top = stack[-1]
    #                 if s[top] == "(":
    #                     stack.pop()
    #                 else:
    #                     stack.append(i)

    #     result = 0
    #     latter = len(s)
    #     while len(stack) != 0:
    #         former = stack.pop()
    #         result = max(result, latter-former-1)
    #         latter = former
    #     result = max(result, latter)
    #     return result


s = Solution()
string = "()"
print s.longestValidParentheses(string)
