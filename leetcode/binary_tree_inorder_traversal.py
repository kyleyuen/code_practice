# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
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
root = TreeNode(1)
second = TreeNode(2)
root.right = second
third = TreeNode(3)
second.left = third
print s.inorderTraversal(root)