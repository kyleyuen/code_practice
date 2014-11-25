class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        record, result = [], []
        self.search(candidates, target, record, result)
        return result

    def search(self, candidates, target, record, result):
        if target == 0:
            temp = sorted(record)
            if temp not in result:
                result.append(temp)

        for num in candidates:
            if target < num:
                break
            record.append(num)
            self.search(candidates, target-num, record, result)
            record.pop()

s = Solution()
candidates = [2, 3, 6, 7]
target = 10
print s.combinationSum(candidates, target)