class Solution:
    # @return a boolean
    def isPalindrome(self, x):
    	if x < 0:
    		return False
        return x == self.reverse_integer(x)


    def reverse_integer(self, x):
    	result = 0
    	while x != 0:
    		reminder = x % 10
    		result = result * 10 + reminder
    		x /= 10
    	return result