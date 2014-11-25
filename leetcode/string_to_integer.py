class Solution:
    # @return an integer
    def atoi(self, s):
        if len(s) == 0:
        	return 0
        
        index = 0
        while s[index] == " ":
        	index += 1
        negative = False
        if s[index] == "-":
        	negative = True
        	index += 1
        elif s[index] == "+":
        	negative = False
        	index += 1
        while s[index] == "0":
        	index += 1

        result = 0
        for i in range(index, len(s)):
        	if not s[i].isdigit():
        		break
        	result = result*10 + int(s[i])
        if negative:
        	result = result * -1

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if result > INT_MAX:
        	return INT_MAX
        elif result < INT_MIN:
        	return INT_MIN
        else:
        	return result


s = Solution()
print s.atoi("  -0012a42")