class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        return haystack.find(needle)


s = Solution()
print s.strStr("231123", "1")