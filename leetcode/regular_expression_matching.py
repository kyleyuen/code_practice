class Rule:
    def __init__(self, c, s=True):
        self.character = c
        self.strict = s
        self.tested = False

    def __repr__(self):
        string_format = "["
        string_format += self.character
        string_format += ", " + str(self.strict)
        string_format += "]"
        return string_format



class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        rule_set = self.process_pattern(p)
        rule_index = 0
        wrong_match = False
        #print rule_set
        for c in s:
            if rule_index == len(rule_set):
                return False

            rule_set[rule_index].tested = True
            # character matched
            if (c == rule_set[rule_index].character) or (rule_set[rule_index].character == "."):
                wrong_match = False
                if rule_set[rule_index].strict:
                    rule_index += 1
            # charcter not matched
            else:
                # return false if not matched with two consective rules
                if wrong_match:
                    return False
                # not matched because of strictness
                if rule_set[rule_index].strict:
                    wrong_match = True
                rule_index += 1

        if (wrong_match) or (rule_index < len(rule_set)-1):
            return False
        if (rule_index == len(rule_set)-1) and (not rule_set[rule_index].tested):
            if len(s) == 0:
                if rule_set[rule_index].strict:
                    return False
            elif (s[-1] != rule_set[rule_index].character) and (rule_set[rule_index] != "."):
                return False
        return True


    def process_pattern(self, p):
        rule_set = []
        index = 0
        while index < len(p)-1:
            r = Rule(p[index])
            index += 1
            if p[index] == '*':
                r.strict = False
                index += 1
            rule_set.append(r)

        if index == len(p) - 1:
            rule_set.append(Rule(p[index]))
        return rule_set


    def match_rule(c, rule):
        if c == rule.character:
            return True


s = Solution()

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
