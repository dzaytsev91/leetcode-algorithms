# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        result = 0
        while stack:
            node = stack.pop()
            if node.val >= L and node.val <= R:
                result += node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
