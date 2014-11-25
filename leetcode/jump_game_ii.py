class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):        
        target = len(A) - 1
        if target < 0:
            return False

        last = 0
        min_step, max_reach = 0, A[0]
        for i in range(len(A)):
            if last < i:
                min_step += 1
                last = max_reach
            if max_reach < i+A[i]:
                max_reach = i+A[i]
            
            if last >= target:
                return min_step
            if max_reach == i:
                return -1
        return min_step



s = Solution()
print s.jump([2,3,1,1,4])