class Solution:
    # @return a string
    def convert(self, s, nRows):
        record = ["" for i in range(nRows)]
        current_row = 0
        direction = True
        for c in s:
        	if direction:
        		record[current_row] += c
        		current_row += 1
        	else:
        		record[current_row] += c
        		current_row -= 1

        	if current_row == nRows:
        		direction = False
        		current_row -= 2
        		current_row = max(current_row, 0)
        	if current_row == 0:
        		direction = True

        result = ""
        for i in range(nRows):
        	result += record[i]
        return result


s = Solution()
print s.convert("PAYPALISHIRING", 1)