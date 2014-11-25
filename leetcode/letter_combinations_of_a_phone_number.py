class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.digit_to_characters = {"1":"", "2":"abc", "3":"edf", "4":"ghi",
        	"5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        records = []
        result = []
        self.convert_digit_to_character(digits, 0, result, records)
        return records


    def convert_digit_to_character(self, digits, index, result, records):
    	if index == len(digits):
    		records.append("".join(result))
    		return

    	characters = self.digit_to_characters[digits[index]]
    	for c in characters:
    		result.append(c)
    		self.convert_digit_to_character(digits, index+1, result, records)
    		result.pop()


s = Solution()
print s.letterCombinations("23")