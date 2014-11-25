class Solution:
    # @return an integer
    def maxArea(self, height):
    	result = 0
        left, right = 0, len(height)-1
        while left != right:
        	area = (right-left) * min(height[left], height[right])
        	if result < area:
        		result = area
        	if height[left] < height[right]:
        		left += 1
        	else:
        		right -= 1
        return result


s = Solution()
height = [1, 2, 3, 4, 5]
print s.maxArea(height)