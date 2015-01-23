class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left, right = 0, len(A)-1

        while left <= right:
            middle = (left+right) / 2
            if A[middle] == target:
                return True

            if A[left] < A[middle]:
                if (A[left] <= target <=A[middle]):
                    right = middle - 1
                else:
                    left = middle + 1
            elif A[left] > A[middle]:
                if (A[middle] <= target <= A[right]):
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                left += 1

        return False


s = Solution()
array = [1, 3, 1, 1, 1]
print s.search(array, 3)