# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                res.append(node.val)
            else:
                # left -> root -> right
                stack.append([node.right, False])
                stack.append([node, True])
                stack.append([node.left, False])
        return res

