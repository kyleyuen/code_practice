class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
    	string_length = len(S)
    	list_length = len(L)
    	word_length = len(L[0])
        states = [-1 for i in range(string_length-word_length)]

        for i in range(len(states)):
        	try:
        		states[i] = L.index(S[i:i+word_length])
        	except ValueError:
        		states[i] = -1
        
        result = []
        i = 0
        while i <= (string_length-word_length*list_length):
        	record = set()
        	matched = True
        	for j in range(list_length):
        		try:
        			index = L.index(S[i+j*word_length:i+(j+1)*word_length])
        			print i, j, index
        			if index in record:
        				matched = False
        				break
        			else:
        				record.add(index)
        		except ValueError:
        			matched = False
        			break

        	if matched:
        		result.append(i)
        		i += word_length * list_length
        	else:
        		i += 1
        return result



s = Solution()
string = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
array = ["fooo","barr","wing","ding","wing"]
print s.findSubstring(string, array)