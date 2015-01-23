# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
            return []
        
        result, stack, temp = [], [], []
        level = 0

        stack.append((root, 0))
        while len(stack) != 0:
            node = stack.pop(0)
            if level != node[1]:
                result.insert(0, temp)
                temp = []
                level += 1
            temp.append(node[0].val)

            if node[0].left:
                stack.append((node[0].left, level+1))
            if node[0].right:
                stack.append((node[0].right, level+1))
        result.insert(0, temp)

        return result

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
b.left = d
print s.levelOrderBottom(a)