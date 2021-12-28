# idea: do dfs but add to stack node + all possible sums and combinations
# of previous nodes. Check when needed value will appear
# in this combinations and count them


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        num = 0
        stack = [(root, [root.val])]
        while stack:
            node, totals = stack.pop()
            num += totals.count(targetSum)
            if node.left:
                stack.append([node.left, [x+node.left.val for x in totals] + [node.left.val]])
            if node.right:
                stack.append([node.right, [x+node.right.val for x in totals] + [node.right.val]])
        return num
