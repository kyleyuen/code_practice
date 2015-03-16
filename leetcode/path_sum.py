# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False

        result = [False]
        self.dfs(root, 0, sum, result)
        return result[0]


    def dfs(self, node, current, target, result):
        if node.left==None and node.right==None:
            current += node.val
            if current == target:
                result[0] = True
            return

        if node.left:
            self.dfs(node.left, current+node.val, target, result)
        if node.right:
            self.dfs(node.right, current+node.val, target, result)


s = Solution()
root = TreeNode(5)
l1 = TreeNode(4)
l2 = TreeNode(11)
l31 = TreeNode(7)
l32 = TreeNode(2)
r1 = TreeNode(8)
r21 = TreeNode(13)
r22 = TreeNode(4)
r3 = TreeNode(1)

root.left = l1
root.right = r1

l1.left = l2
l2.left = l31
l2.right = l32

r1.left = r21
r1.right = r22
r22.right = r3

print s.hasPathSum(root, 22)