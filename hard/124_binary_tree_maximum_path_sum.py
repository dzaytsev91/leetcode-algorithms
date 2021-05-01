# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root):
        if root is None:
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))

        self.max_sum = max(self.max_sum, root.val + left + right)
        return max(left, right) + root.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
