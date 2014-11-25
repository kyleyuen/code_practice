class Solution:
    # @return an integer
    def reverse(self, x):
    	negative = False
    	string_format = str(x)
    	if x < 0:
    		negative = True
        	string_format = string_format[1:]
        	
        result = ""
        for c in reversed(string_format):
        	result += c
        if negative:
        	result = "-" + result
        return int(result)


s = Solution()
print s.reverse(-123)