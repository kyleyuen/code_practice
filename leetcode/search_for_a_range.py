class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = self.find_left_bound(A, target)
        right = self.find_right_bound(A, target)
        return [left, right]

    def find_left_bound(self, array, target):
        start, end = 0, len(array)-1
        while start <= end:
            if array[start] == target:
                return start
            middle = (start+end) / 2
            if array[middle] < target:
                start = middle+1
            elif array[middle] > target:
                end = middle-1
            else:
                start += 1
        return -1


    def find_right_bound(self, array, target):
        start, end = 0, len(array)-1
        while start <= end:
            print start, end
            if array[end] == target:
                return end
            middle = (start+end) / 2
            if array[middle] < target:
                start = middle+1
            elif array[middle] > target:
                end = middle-1
            else:
                end -= 1
        return -1


s = Solution()
array = [5, 7, 7, 8, 8, 10]
print s.searchRange(array, 10)