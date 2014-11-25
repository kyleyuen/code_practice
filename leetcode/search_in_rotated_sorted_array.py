class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left, right = 0, len(A)-1

        while left <= right:
            middle = (left+right) / 2
            if A[middle] == target:
                return middle

            if A[left] <= A[middle]:
                if (A[left]<=target) and (target<=A[middle]):
                    right = middle
                else:
                    left = middle + 1
            else:
                if (A[middle]<=target) and (target<=A[right]):
                    left = middle + 1
                else:
                    right = middle

        return -1


s = Solution()
array = [1]
print s.search(array, 0)