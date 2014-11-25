class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        record, result = [], []
        self.search(candidates, 0, target, record, result)
        return result

    def search(self, candidates, index, target, record, result):
        if target == 0:
            temp = sorted(record)
            if temp not in result:
                result.append(temp)

        for i in range(index, len(candidates)):
            if target < candidates[i]:
                break
            record.append(candidates[i])
            self.search(candidates, i+1, target-candidates[i], record, result)
            record.pop()

s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print s.combinationSum2(candidates, target)