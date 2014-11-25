class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
		record = {}
		for i in range(len(num)):
			another = target-num[i]
			if another in record:
				return record[another], i+1
			else:
				record[num[i]] = i+1


s = Solution()
num = [0, 2, 4, 0]
target = 0
print s.twoSum(num, target)