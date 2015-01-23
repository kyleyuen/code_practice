class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)

        index, length = 2, 2
        while index < len(A):
            if A[index] != A[length-2]:
                A[length] = A[index]
                length += 1
            index += 1
        return length


s = Solution()
print s.removeDuplicates([1,1,1,2])