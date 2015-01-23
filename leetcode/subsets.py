class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        record, result = [], []
        self.generate_subset(S, 0, record, result)
        return result


    def generate_subset(self, array, index, record, result):
        if index == len(array):
            result.append(record[:])
            return

        record.append(array[index])
        self.generate_subset(array, index+1, record, result)
        record.pop()
        self.generate_subset(array, index+1, record, result)


s = Solution()
print s.subsets([4, 1, 0])