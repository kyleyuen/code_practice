class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_numbers = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50,
    		"XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
    	index = 0
    	result = 0
    	while index < len(s):
    		if (index < len(s)-1) and (s[index:index+2] in roman_numbers):
    			result += roman_numbers[s[index:index+2]]
    			index += 2
    		else:
    			result += roman_numbers[s[index]]
    			index += 1
    	return result


s = Solution()
print s.romanToInt("MCDLXXVI")