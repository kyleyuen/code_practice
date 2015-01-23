# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        
        result, stack, temp = [], [], []
        level = 0
        order = True

        stack.append((root, 0))
        while len(stack) != 0:
            if level != stack[0][1]:
                result.append(temp)
                temp = []
                level += 1

                stack.reverse()
                order = not order
                
            node = stack.pop(0)
            if node[0] == None:
                continue
            temp.append(node[0].val)

            if order:
                stack.append((node[0].left, level+1))
                stack.append((node[0].right, level+1))
            else:
                stack.append((node[0].right, level+1))
                stack.append((node[0].left, level+1))
        return result

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
print s.zigzagLevelOrder(a)