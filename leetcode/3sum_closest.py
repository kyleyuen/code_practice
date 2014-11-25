class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num = sorted(num)
        result = 1e6
        for index in range(len(num)-2):
            left, right = index+1, len(num)-1
            while left < right:
                summation = num[index]+num[left]+num[right]
                if abs(target-result) > abs(target-summation):
                	result = summation

                if summation < target:
                    left += 1
                else:
                    right -= 1

        return result


s = Solution()
#num = [-13,11,11,0,-5,-14,12,-11,-11,-14,-3,0,-3,12,-1,-9,-5,-13,9,-7,-2,9,-1,4,-6,-13,-7,10,10,9,7,13,5,4,-2,7,5,-13,11,10,-12,-14,-5,-8,13,2,-2,-14,4,-8,-6,-13,9,8,6,10,2,6,5,-10,0,-11,-12,12,8,-7,-4,-9,-13,-7,8,12,-14,10,-10,14,-3,3,-15,-14,3,-14,10,-11,1,1,14,-11,14,4,-6,-1,0,-11,-12,-14,-11,0,14,-9,0,7,-12,1,-6]
#num = [-1, 2, 1, -4]
num = [1, 1, 1, 0]
print s.threeSumClosest(num, 100)
#s.threeSum(num)