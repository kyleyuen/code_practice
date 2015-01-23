# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        pair = []
        travelsal = self.inorderTraversal(root)
        for i in range(1, len(travelsal)):
            if travelsal[i-1] >= travelsal[i]:
                pair.append(travelsal[i-1])
                pair.append(travelsal[i])
        
        first = self.get_node_by_value(root, min(pair))
        first.val = max(pair)
        second = self.get_node_by_value(root, max(pair))
        second.val = min(pair)
        
        return root

    def get_node_by_value(self, node, value):
        if node.left:
            result = self.get_node_by_value(node.left, value)
            if result != None:
                return result
        
        if node.val == value:
            return node

        if node.right:
            result = self.get_node_by_value(node.right, value)
            if result != None:
                return result

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
a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(4)
root.left = c
root.right = b
b.right = a
print s.inorderTraversal(s.recoverTree(root))