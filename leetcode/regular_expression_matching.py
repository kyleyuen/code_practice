class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if len(s) == 0:
            return len(p) == 0
        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1:
            return (len(s)==1 and self.match_first(s[0], p[0]))
        
        if p[1] == "*":
            if self.isMatch(s, p[2:]):
                return True

            for i in range(len(s)):
                if not self.match_first(s[i], p[0]):
                    break
                if self.isMatch(s[i+1:], p):
                    return True
        else:
            if not self.match_first(s[0], p[0]):
                return False
            return self.isMatch(s[1:], p[1:])
        return False


    def match_first(self, a, b):
        return (a==b) or (a!='' and b==".")


s = Solution()
print s.isMatch("aa", "a")
print s.isMatch("a", ".*..a*")
print s.isMatch("ab", "a*")

print s.isMatch("ab", ".*c")
print s.isMatch("abcd", "d*")

print s.isMatch("aa","a")
print s.isMatch("aa","aa")
print s.isMatch("aaa","aa")
print s.isMatch("aa", "a*")
print s.isMatch("aa", ".*")
print s.isMatch("ab", ".*")

print s.isMatch("aab", "c*a*b")
