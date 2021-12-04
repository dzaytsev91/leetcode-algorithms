# idea: using bfs add nodes by level to stack from left to right
# than add last element in level to result


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [(root,)]
        while stack:
            level = stack.pop()
            result.append(level[-1].val)
            current_lvl = []
            for node in level:
                if node.left:
                    current_lvl.append(node.left)
                if node.right:
                    current_lvl.append(node.right)
            if current_lvl:
                stack.append(current_lvl)
        return result
