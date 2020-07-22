# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        result = []
        levels = [root]
        while levels:
            result.append(sum([x.val for x in levels]))
            new_levels = []
            for level in levels:
                if level.right:
                    new_levels.append(level.right)
                if level.left:
                    new_levels.append(level.left)
            levels = new_levels
        return result.index(max(result)) + 1
