class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))

s = Solution()
num1 = "11111111111111111111111111111"
num2 = "22222222222222222222222222222"
print s.multiply(num1, num2)