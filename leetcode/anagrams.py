class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        records = {}
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            word_characters = str(self.collect_characters(word))
            if word_characters in records:
                records[word_characters].append(i)
            else:
                records[word_characters] = [i]

        result = []
        for (word, words_list) in records.items():
            if len(words_list) > 1:
                for i in words_list:
                    result.append(strs[i])
        return result


    def collect_characters(self, word):
        result = {}
        for c in word:
            if c in result:
                result[c] += 1
            else:
                result[c] = 1
        return result


s = Solution()
strs = ["cat","rye","aye","dog", "god","cud","cat","old","fop","bra"]
print s.anagrams(strs)