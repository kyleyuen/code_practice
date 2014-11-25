class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num = sorted(num)
        result = []
        index = 0
        while index < len(num)-2:
            left, right = index+1, len(num)-1
            while left < right:
                summation = num[index]+num[left]+num[right]
                if summation < 0:
                    left += 1
                # add to result if condition statisfied
                elif summation == 0:
                    result.append([num[index],num[left],num[right]])                    
                    # skip duplicate elements from left to right
                    left += 1
                    while (left<right) and (num[left-1]==num[left]):
                        left += 1
                    
                    # skip duplicate elements from right to left
                    right -= 1
                    while (left<right) and (num[right]==num[right+1]):
                        right -= 1
                else:
                    right -= 1

            index += 1
            while (index<len(num)-2) and (num[index-1]==num[index]):
                index += 1

        return result


s = Solution()
#num = [-13,11,11,0,-5,-14,12,-11,-11,-14,-3,0,-3,12,-1,-9,-5,-13,9,-7,-2,9,-1,4,-6,-13,-7,10,10,9,7,13,5,4,-2,7,5,-13,11,10,-12,-14,-5,-8,13,2,-2,-14,4,-8,-6,-13,9,8,6,10,2,6,5,-10,0,-11,-12,12,8,-7,-4,-9,-13,-7,8,12,-14,10,-10,14,-3,3,-15,-14,3,-14,10,-11,1,1,14,-11,14,4,-6,-1,0,-11,-12,-14,-11,0,14,-9,0,7,-12,1,-6]
num = [-1, 0, 1, 2, -1, -4]
print s.threeSum(num)
#s.threeSum(num)