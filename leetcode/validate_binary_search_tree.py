# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        traversal = self.inorderTraversal(root)
        for i in range(1, len(traversal)):
            if traversal[i-1] >= traversal[i]:
                return False
        return True

    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []
        if root:
            self.do_inorder_traversal(root, result)
        return result

    def do_inorder_traversal(self, node, result):
        if node.left:
            self.do_inorder_traversal(node.left, result)

        result.append(node.val)
        
        if node.right:
            self.do_inorder_traversal(node.right, result)


s = Solution()
root = TreeNode(2)
second = TreeNode(1)
third = TreeNode(3)
root.left = second
root.right = third
print s.isValidBST(root)