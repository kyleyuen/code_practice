class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        root = 1.0
        sigma = 1e-6
        while True:
            previous = root
            root = (root + x/root) / 2
            if abs(root-previous) < sigma:
                return int(root)


s = Solution()
print s.sqrt(35)