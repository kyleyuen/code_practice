class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        words = s.split()
        if len(words) == 0:
            return 0
        else:
            return len(words[-1])


s = Solution()
print s.lengthOfLastWord("hello, world")
print s.lengthOfLastWord("")