# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p and q:
            if (p.val==q.val) \
            and (self.isSameTree(p.left, q.left)) \
            and (self.isSameTree(p.right, q.right)):
                return True
        elif (p==None) and (q==None):
            return True
        
        return False


s = Solution()
root = TreeNode(1)
second = TreeNode(2)
third = TreeNode(3)
root.right = second
second.left = third

t_root = TreeNode(1)
t_second = TreeNode(2)
t_third = TreeNode(3)
t_root.right = t_second
t_second.right = t_third

print s.isSameTree(root, t_root)