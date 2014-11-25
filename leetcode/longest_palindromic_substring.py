class Solution:
    # @return a string
    def longestPalindrome(self, s):
        
        for i in range(len(s)):
        	if (current*2 <= i) and (s[i] == s[i-current*2]):
        		current += 1
        	else:
        		current = 1
        	if result < current:
        		result = current

        return result*2-1
        

s = Solution()
print s.longestPalindrome("bbbbbb")