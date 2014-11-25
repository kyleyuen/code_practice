class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        result, record = -1e6, 0
        for num in A:
            record += num
            if result < record:
                result = record
            if record < 0:
                record = 0
        return result


s = Solution()
array = [-2,1,-3,4,-1,2,1,-5,4]
print s.maxSubArray(array)