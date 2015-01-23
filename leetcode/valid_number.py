class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
    	print isinstance("2e10", float)
        try:
        	float(s)
        except ValueError:
        	return False
        return True


s = Solution()
number = "2e10"
print s.isNumber("a")