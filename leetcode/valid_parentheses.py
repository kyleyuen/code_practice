class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
                continue

            if len(stack) == 0:
                return False

            current = stack.pop()
            if current=="(" and c==")":
                pass
            elif current=="[" and c=="]":
                pass
            elif current =="{" and c=="}":
                pass
            else:
                return False
        return len(stack) == 0


s = Solution()
print s.isValid("()[]{[}]")