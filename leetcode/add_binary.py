class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        index_a = len(a)-1
        index_b = len(b)-1

        result = ""
        carry = 0
        while index_a >= 0 and index_b >= 0:
            digit = int(a[index_a]) + int(b[index_b]) + carry
            if digit > 1:
                digit -= 2
                carry = 1
            else:
                carry = 0
            result = str(digit) + result

            index_a -= 1
            index_b -= 1

        while index_a >= 0:
            digit = int(a[index_a]) + carry
            if digit > 1:
                digit -= 2
                carry = 1
            else:
                carry = 0
            result = str(digit) + result
            
            index_a -= 1

        while index_b >= 0:
            digit = int(b[index_b]) + carry
            if digit > 1:
                digit -= 2
                carry = 1
            else:
                carry = 0
            result = str(digit) + result
            
            index_b -= 1

        if carry == 1:
            result = "1" + result
        return result


s = Solution()
a = "111110"
b = "11111"
print s.addBinary(a, b)