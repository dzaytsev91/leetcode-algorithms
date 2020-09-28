# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        stack = [root]
        while stack:
            level_result = []
            nodes = []
            while stack:
                node = stack.pop(0)
                if not node:
                    continue
                nodes.append(node.left)
                nodes.append(node.right)
                level_result.append(node.val)
            stack = nodes
            if level_result:
                result.append(level_result)
        return result
