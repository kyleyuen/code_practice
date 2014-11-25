class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        begin, end = 0, len(A)-1
        while begin <= end:
            if begin == end:
                if A[begin] >= target:
                    return begin
                else:
                    return end + 1
            elif (end-begin) == 1:
                if A[end] < target:
                    return end + 1
                elif A[begin] < target:
                    return begin + 1
                else:
                    return begin

            middle = (begin+end) / 2
            if A[middle] < target:
                begin = middle
            elif A[middle] > target:
                end = middle
            else:
                return middle


s = Solution()
# array = [1,3,5,6]
# print s.searchInsert(array, 5)
# print s.searchInsert(array, 2)
# print s.searchInsert(array, 7)
# print s.searchInsert(array, 3)
array = [1]
print s.searchInsert(array, 1)