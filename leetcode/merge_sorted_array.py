class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        m -= 1
        n -= 1
        position = m+n+1
        while m>=0 and n>=0:
            if A[m] > B[n]:
                A[position] = A[m]
                m -= 1
            else:
                A[position] = B[n]
                n -= 1
            position -= 1
        
        while n >= 0:
            print position, n
            A[position] = B[n]
            n -= 1
            position -= 1


s = Solution()
array_A = [1, 3, 5, 0, 0, 0]
array_B = [2, 4, 6]
s.merge(array_A, 3, array_B, 3)