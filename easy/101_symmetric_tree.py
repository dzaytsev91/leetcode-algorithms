# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if right and left:
            return left.val == right.val and self.check(left.right, right.left) and self.check(left.left, right.right)
        return left == right
