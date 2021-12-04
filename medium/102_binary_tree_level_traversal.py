# idea: using BFS we should add nodes to stack level by level
# than agg lvl values and add to result

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        stack = [(root,)]
        while stack:
            level = stack.pop()
            current_lvl_values = []
            next_lvl = []
            for node in level:
                current_lvl_values.append(node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)

            if current_lvl_values:
                result.append(current_lvl_values)
            if next_lvl:
                stack.append(next_lvl)
        return result
