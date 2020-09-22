# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        max_sum = 0
        stack = [root]
        while stack:
            values = []
            max_sum = 0
            while stack:
                root = stack.pop()
                if root.left:
                    values.append(root.left)
                if root.right:
                    values.append(root.right)
                max_sum += root.val
            stack.extend(values)
        return max_sum
