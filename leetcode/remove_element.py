class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
    	if len(A) == 0:
    		return 0

        index, replace_index = 0, len(A)-1
        while index < len(A):
        	if index > replace_index:
        		return index

        	if A[index] == elem:
        		A[index] = A[replace_index]
        		A[replace_index] = elem
        		replace_index -= 1
        	else:
        		index += 1


s = Solution()
array = [1, 1, 4]
print s.removeElement(array, 1)