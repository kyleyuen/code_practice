class Solution:
    # @return a string
    def countAndSay(self, n):
        number = "1"
        for i in range(n-1):
            number = self.generate_next(number)
        return number


    def generate_next(self, digits):
        result = ""
        left, right = 0, 0
        while right < len(digits):
            if digits[left] == digits[right]:
                right += 1
            else:
                result += str(right-left) + digits[left]
                left = right
        result += str(right-left) + digits[left]
        return result


s = Solution()
print s.countAndSay(20)