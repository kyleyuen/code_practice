class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        left, right = 0, len(A)-1
        max_left, max_right = 0, 0
        while left < right:
            if A[left] < A[right]:
                if max_left < A[left]:
                    max_left = A[left]
                else:
                    result += (max_left-A[left])
                left += 1
            else:
                if max_right < A[right]:
                    max_right = A[right]
                else:
                    result += (max_right-A[right])
                right -= 1
        return result


s = Solution()
array = [0,1,0,2,1,0,1,3,2,1,2,1]
array = [4, 2, 3]
print s.trap(array)