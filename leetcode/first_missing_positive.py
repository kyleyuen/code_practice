class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(len(A)):
        	x = i
        	while x >= 0 and A[x] != x:
        		print A
        		raw_input()
        		
        		y = A[x]
        		A[x] = A[y]
        		A[y] = y
        		x = A[x]
        
        print A
        for i in range(1, len(A)):
        	if A[i] != i:
        		return i
        return len(A)


s = Solution()
array = [2, 3, 1, -1]
print s.firstMissingPositive(array)