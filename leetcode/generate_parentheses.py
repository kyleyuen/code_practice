class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        records = []
        result = []
        self.dfs(n, n, result, records)
        return records


    def dfs(self, left, right, result, records):
    	if left==0 and right==0:
    		records.append("".join(result))
    		return

    	if left != 0:
    		result.append("(")
    		self.dfs(left-1, right, result, records)
    		result.pop()
    		
    	if left < right:
    		result.append(")")
    		self.dfs(left, right-1, result, records)
    		result.pop()


s = Solution()
print s.generateParenthesis(3)