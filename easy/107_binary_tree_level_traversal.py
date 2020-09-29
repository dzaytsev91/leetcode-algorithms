# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        result = []
        while stack:
            nodes = []
            local_result = []
            while stack:
                node = stack.pop(0)
                if not node:
                    continue
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                local_result.append(node.val)
            result.insert(0, local_result)
            stack = nodes
        return result
