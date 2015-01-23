class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        for i in range(n):
            target = A[i]
            while (target>0) and (target<=n) and (A[target-1]!=target):
                new_target = A[target-1]
                A[target-1] = target
                target = new_target
        
        for i in range(n):
            if A[i] != i+1:
                return i+1
        return n+1
        

s = Solution()
array = [3, 4, 1, -1]
#array = [1, 2, 0]
print s.firstMissingPositive(array)