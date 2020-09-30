# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [[root, 0]]
        while stack:
            node, max_val = stack.pop()

            if not node.left and not node.right and node.val + max_val == sum:
                return True

            if node.left:
                stack.append([node.left, node.val + max_val])
            if node.right:
                stack.append([node.right, node.val + max_val])
        return False
