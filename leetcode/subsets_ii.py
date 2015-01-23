class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        record, result = [], set()
        self.generate_subset(S, 0, record, result)

        real_result = []
        for s in result:
            real_result.append(list(s))
        return real_result


    def generate_subset(self, array, index, record, result):
        if index == len(array):
            result.add(tuple(record))
            return

        record.append(array[index])
        self.generate_subset(array, index+1, record, result)
        record.pop()
        self.generate_subset(array, index+1, record, result)


s = Solution()
array = [1, 2, 2]
print s.subsetsWithDup(array)