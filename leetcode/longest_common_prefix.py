class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
    	if len(strs) == 0:
    		return ""
        first_string = strs[0]
        for i in range(0, len(first_string)):
        	prefix = first_string[0:i+1]
        	for j in range(1, len(strs)):
        		if not strs[j].startswith(prefix):
        			return first_string[0:i]
        return first_string


s = Solution()
strs = ["a", "aab", "aac"]
print s.longestCommonPrefix(strs)