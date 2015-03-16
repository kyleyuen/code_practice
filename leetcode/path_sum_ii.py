# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root == None:
            return []

        result, record = [], []
        self.dfs(root, 0, sum, record, result)
        return result


    def dfs(self, node, current, target, record, result):
        if node.left==None and node.right==None:
            current += node.val
            record.append(node.val)
            if current == target:
                result.append(record[:])
            record.pop()
            return

        if node.left:
            record.append(node.val)
            self.dfs(node.left, current+node.val, target, record, result)
            record.pop()
        if node.right:
            record.append(node.val)
            self.dfs(node.right, current+node.val, target, record, result)
            record.pop()


s = Solution()
root = TreeNode(5)
l1 = TreeNode(4)
l2 = TreeNode(11)
l31 = TreeNode(7)
l32 = TreeNode(2)
r1 = TreeNode(8)
r21 = TreeNode(13)
r22 = TreeNode(4)
r31 = TreeNode(5)
r32 = TreeNode(1)

root.left = l1
root.right = r1

l1.left = l2
l2.left = l31
l2.right = l32

r1.left = r21
r1.right = r22
r22.left = r31
r22.right = r32

print s.pathSum(root, 22)