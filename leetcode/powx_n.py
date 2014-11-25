class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1.0 / self.pow(x, -n)
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            value = self.pow(x, n/2)
            return value ** 2
        elif n % 2 == 1:
            value = self.pow(x, n/2)
            return value ** 2 * x


s = Solution()
print s.pow(0.00001, 2147483647)