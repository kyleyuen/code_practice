class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        left, right = len(num)-2, len(num)-1 
        while left >= 0:
            if num[left] < num[left+1]:
                break
            left -= 1
        if left < 0:
            return sorted(num)

        while right > 0:
            if num[left] < num[right]:
                break
            right -= 1


        temp = num[left]
        num[left] = num[right]
        num[right] = temp

        left += 1
        right = len(num)-1
        while left < right:
            temp = num[left]
            num[left] = num[right]
            num[right] = temp

            left += 1
            right -= 1
        return num


s = Solution()
num = [4, 3, 2, 1, 5]
print s.nextPermutation(num)