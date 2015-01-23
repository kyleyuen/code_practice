class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        record, result = [], []
        self.generate_combination(range(1, n+1), 0, k, record, result)
        return result


    def generate_combination(self, array, index, target, record, result):
        if target == 0:
            result.append(record[:])
            return
        if index == len(array):
        	return

        for i in range(index, len(array)):
            record.append(array[i])
            self.generate_combination(array, i+1, target-1, record, result)
            record.pop()


s = Solution()
print s.combine(50, 2)