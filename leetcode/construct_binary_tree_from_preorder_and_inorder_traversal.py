# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) != len(inorder):
            return None
        if len(preorder)==0 or len(inorder)==0:
            return None
        return self.do_build_tree(preorder, 0, len(preorder), inorder, 0, len(inorder))


    def do_build_tree(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if (pre_start>=pre_end) or (in_start>=in_end):
            return None
        
        position = 0
        while inorder[in_start+position] != preorder[pre_start]:
            position += 1
        if in_start+position >= in_end:
            return None

        root = TreeNode(preorder[pre_start])
        root.left = self.do_build_tree(preorder, pre_start+1, pre_start+1+position, inorder, in_start, in_start+position)
        root.right = self.do_build_tree(preorder, pre_start+1+position, pre_end, inorder, in_start+1+position, in_end)
        return root


def do_preorder_traversal(node, result):
    result.append(node.val)

    if node.left:
        do_preorder_traversal(node.left, result)
    
    if node.right:
        do_preorder_traversal(node.right, result)


def preorderTraversal(root):
        result = []
        if root:
            do_preorder_traversal(root, result)
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
preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder =  [4, 7, 2, 1, 5, 3, 8, 6]
tree = s.buildTree(preorder, inorder)
print preorderTraversal(tree)
print inorderTraversal(tree)