# Definition for a  binary tree node# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:
            return []
        
        result, stack, temp = [], [], []
        level = 0

        stack.append((root, 0))
        while len(stack) != 0:
            node = stack.pop(0)
            if level != node[1]:
                result.append(temp)
                temp = []
                level += 1
            temp.append(node[0].val)

            if node[0].left:
                stack.append((node[0].left, level+1))
            if node[0].right:
                stack.append((node[0].right, level+1))
        result.append(temp)

        return result

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
b.left = d
print s.levelOrder(a)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        
        level = 1
        stack = []
        stack.append((root, level))
        while len(stack) != 0:
            node = stack.pop(0)
            if level != node[1]:
                level += 1
            if node[0].left:
                stack.append((node[0].left, level+1))
            if node[0].right:
                stack.append((node[0].right, level+1))
        return level


s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
# b.right = e
print s.maxDepth(a)