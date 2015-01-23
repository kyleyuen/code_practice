class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        left, right = 0, len(A)-1
        i = 0
        while i <= right:
            if A[i] == 0:
                A[left] = 0
                left += 1
            elif A[i] == 2:
                A[i], A[right] = A[right], A[i]
                right -= 1
                continue
            i += 1

        for i in range(left, right+1):
            A[i] = 1

s = Solution()
print s.sortColors([2,1,0, 1,2,0,0,2,1,1])