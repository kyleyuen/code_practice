class Solution:
    # @return a string
    def intToRoman(self, num):
    	roman_numbers = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L",
    		90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
    	units = sorted(roman_numbers)
    	index = len(units)-1
    	result = ""
    	while (index >= 0):
    		while num >= units[index]:
    			num -= units[index]
    			result += roman_numbers[units[index]]
    		index -= 1
    	return result
    	


s = Solution()
print s.intToRoman(99)