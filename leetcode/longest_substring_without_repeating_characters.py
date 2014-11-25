class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
    	if len(s) == 0:
    		return 0

    	current, result = 1, 1
    	record = {}
    	record[s[0]] = 0
    	for i in range(1, len(s)):
    		if (s[i] not in record) or (current<i-record[s[i]]):
    			current += 1
    		else:
    			current = i-record[s[i]]
    		record[s[i]] = i
    		if result < current:
    			result = current
    	return result


s = Solution()
print s.lengthOfLongestSubstring("abcabc")
print s.lengthOfLongestSubstring("ruowzgiooobpple")