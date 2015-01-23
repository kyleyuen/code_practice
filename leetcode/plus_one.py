class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
        
        if carry == 1:
            digits.insert(0, 1)
        return digits


s = Solution()
digits = [9, 9, 9, 0]
print s.plusOne(digits)