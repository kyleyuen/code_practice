class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        indices = []

        result = 0
        for i in range(len(height)):
            while (len(indices)>0) and (height[i]<=height[indices[-1]]):
                temp = height[indices[-1]]
                indices.pop()

                if len(indices) > 0:
                    width = indices[-1]
                else:
                    width = -1

                area = temp * (i-width-1)
                if result < area:
                    result = area
                print area
            indices.append(i)
        return result


s = Solution()
array = [2,1,5,6,2,3]
print s.largestRectangleArea(array)