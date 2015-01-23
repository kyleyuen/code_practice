class Solution:
    # @return a list of integers
    def grayCode(self, n):
        result = self.generate_gray_code(n)
        for i in range(len(result)):
            result[i] = int(result[i], 2)
        return result

    def generate_gray_code(self, n):
        if n == 0:
            return ["0"]
        elif n == 1:
            return ["0", "1"]
        else:
            numbers = self.generate_gray_code(n-1)
            result = []
            for num in numbers:
                result.append("0"+num)
            for num in reversed(numbers):
                result.append("1"+num)
            return result


s = Solution()
print s.grayCode(0)