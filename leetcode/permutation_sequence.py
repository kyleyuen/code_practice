class Solution:
    # @return a string
    def getPermutation(self, n, k):
        if n == 1:
            factor = 0
        else:
            factor = 1
            for i in range(1, n):
                factor *= i
        k -= 1
        divisor = n-1

        result = ""
        state = range(1, n+1)
        for i in range(n-1):
            index = k / factor
            result += str(state[index])
            for j in range(index, divisor):
                state[j] = state[j+1]

            k %= factor
            if divisor == 1:
                factor = 0
                break
            else:
                factor /= divisor
            divisor -= 1

        result += str(state[factor])
        return result


s = Solution()
print s.getPermutation(1, 1)
print s.getPermutation(2, 1)
print s.getPermutation(2, 2)
print s.getPermutation(3, 2)
print s.getPermutation(9, 171669)