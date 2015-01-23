class Solution:
    # @return a string
    def minWindow(self, S, T):
        characters = {}
        for c in T:
            if c in characters:
                characters[c] -= 1
            else:
                characters[c] = -1

        UNREACHABLE = 1e6
        shortest_index, shortest_length = 0, UNREACHABLE
        counter = len(characters)
        left, right = 0, 0
        while left<len(S) and right<len(S):
            if S[right] in characters:
                characters[S[right]] += 1
                if characters[S[right]] == 0:
                    counter -= 1
            else:
                characters[S[right]] = 1
            right += 1

            while counter == 0:
                length = right-left
                if shortest_length > length:
                    shortest_length = length
                    shortest_index = left

                characters[S[left]] -= 1
                if characters[S[left]] < 0:
                    counter += 1                
                left += 1

        if shortest_length == UNREACHABLE:
            return ""
        return S[shortest_index:shortest_index+shortest_length]


s = Solution()
source = "ADOBECODEBANC"
target = "ABC"
print s.minWindow(source, target)