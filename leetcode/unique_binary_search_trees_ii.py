# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.do_generate_trees(1, n)


    def do_generate_trees(self, start, end):
        result = []
        if start > end:
            result.append(None)
        
        for i in range(start, end+1):
            left_tree = self.do_generate_trees(start, i-1)
            right_tree = self.do_generate_trees(i+1, end)

            for left_node in left_tree:
                for right_node in right_tree:
                    node = TreeNode(i)
                    node.left = left_node
                    node.right = right_node
                    result.append(node)
        return result


def do_inorder_traversal(node, result):
    if node.left:
        do_inorder_traversal(node.left, result)

    result.append(node.val)
    
    if node.right:
        do_inorder_traversal(node.right, result)


def inorderTraversal(root):
        result = []
        if root:
            do_inorder_traversal(root, result)
        return result


s = Solution()
result = s.generateTrees(4)
for root in result:
    print inorderTraversal(root)