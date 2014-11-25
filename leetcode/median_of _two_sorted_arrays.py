class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if m > n:
            return self.findMedianSortedArrays(B, A)

        half_length = (m+n-1) / 2
        left, right = 0, min(half_length, m)
        while left < right:
            medium_A = (left+right) / 2
            medium_B = half_length - medium_A
            if A[medium_A] < B[medium_B]:
                left = medium_A + 1
            else:
                right = medium_A

        # after binary search, we almost get the median because it must be between
        # these 4 numbers: A[left-1], A[left], B[half_length-left], and B[half_length-left+1] 

        # if (n+m) is odd, the median is the larger one between A[left-1] and B[half_length-left].
        # and there are some corner cases we need to take care of.
        a = -1e9
        if left > 0:
            a = A[left-1]
        if half_length-left >= 0:
            a = max(a, B[half_length-left])
        if ((m+n)%2) == 1:
            return a;

        # if (n+m) is even, the median can be calculated by 
        # median = (max(A[left-1], B[half_length-left]) + min(A[left], B[half_length-left+1]) / 2.0
        # also, there are some corner cases to take care of.
        b = 1e9
        if left < m:
            b = A[left]
        if half_length - left + 1 < n:
            b = min(b, B[half_length-left+1])
        return (a+b) / 2.0


s = Solution()
A = [1, 1]
B = [1, 2]
print s.findMedianSortedArrays(A, B)