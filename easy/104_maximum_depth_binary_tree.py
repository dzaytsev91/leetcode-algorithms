# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [(root, 1)]
        while stack:
            node, lvl = stack.pop()
            if not node:
                continue
            result = max(result, lvl)
            if node.left:
                stack.append([node.left, lvl+1])
            if node.right:
                stack.append([node.right, lvl+1])
        return result
