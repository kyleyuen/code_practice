class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
    	num = sorted(num)
        result = []
        times = reduce(lambda x, y: x*y, range(1, len(num)+1))
        for i in range(times):
            result.append(num[:])
            self.next_permutation(num)
        return result


    def next_permutation(self, num):
        first, second = len(num)-2, len(num)-1
        while first >= 0:
            if num[first] < num[first+1]:
                break
            first -= 1

        if first < 0:
            return sorted(num)

        while second > 0:
            if num[first] < num[second]:
                break
            second -= 1

        num[first], num[second] = num[second], num[first]
        num[first+1:] = reversed(num[first+1:])
        return num


s = Solution()
num = [1, 2, 3]
print s.permute(num)