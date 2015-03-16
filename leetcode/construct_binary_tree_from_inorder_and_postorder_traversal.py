# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) != len(postorder):
            return None
        if len(inorder)==0 or len(postorder)==0:
            return None
        return self.do_build_tree(inorder, 0, len(inorder), postorder, 0, len(postorder))


    def do_build_tree(self, inorder, in_start, in_end, postorder, post_start, post_end):
        if (in_start>=in_end) or (post_start>=post_end):
            return None
        
        position = 0
        while inorder[in_start+position] != postorder[post_end-1]:
            position += 1
        if in_start+position >= in_end:
            return None

        root = TreeNode(postorder[post_end-1])
        root.left = self.do_build_tree(inorder, in_start, in_start+position, postorder, post_start, post_start+position)
        root.right = self.do_build_tree(inorder, in_start+1+position, in_end, postorder, post_start+position, post_end-1)
        return root


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


def do_postorder_traversal(node, result):
    if node.left:
        do_postorder_traversal(node.left, result)
    
    if node.right:
        do_postorder_traversal(node.right, result)

    result.append(node.val)


def postorderTraversal(root):
        result = []
        if root:
            do_postorder_traversal(root, result)
        return result

s = Solution()
preorder =  [1, 2, 4, 7, 3, 5, 6, 8]
inorder =   [4, 7, 2, 1, 5, 3, 8, 6]
postorder = [7, 4, 2, 5, 8, 6, 3, 1]
tree = s.buildTree(inorder, postorder)
print inorderTraversal(tree)
print postorderTraversal(tree)