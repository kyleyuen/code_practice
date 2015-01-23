class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        result = []
        left, right = 0, 1
        while right <= len(words):
            length = len(words[left])
            while True:
                if (right>=len(words)) or (length+len(words[right])>=L):
                    break
                length += len(words[right])+1
                right += 1
            last_line = right == len(words)
            result.append(self.generate_line(words, left, right, L, last_line))
            left = right
            right += 1
        return result


    def generate_line(self, words, left, right, L, last_line):
        spaces_number = right-left-1
        result = ""
        if spaces_number == 0:
            result = words[left]
            for i in range(L-len(words[left])):
                result += " "
        elif last_line:
            for i in range(left, right):
                result += words[i]
                L -= len(words[i])
                if L > 0:
                    result += " "
                    L -= 1
            while L > 0:
                result += " "
                L -= 1
        else:
            spaces = [0 for i in range(spaces_number)]
            for i in range(left, right):
                L -= len(words[i])

            index = 0
            while L > 0:
                spaces[index] += 1
                index += 1
                index %= spaces_number
                L -= 1

            for i in range(spaces_number):
                result += words[left+i]
                for j in range(spaces[i]):
                    result += " "
            result += words[right-1]
        return result


s = Solution()
words = ["What","must","be","shall","be."]
words = ["This", "is", "an", "example", "of", "text", "justification."]
length = 14
print s.fullJustify(words, length)