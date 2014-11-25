class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0

        result = 1
        for i in range(1, len(A)):
            if A[i-1] != A[i]:
                A[result] = A[i]
                result += 1
        return result


s = Solution()
array = []
print s.removeDuplicates(array)