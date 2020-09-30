# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        s1 = [root]
        s2 = []
        level = []
        result = []
        while s1 or s2:
            while s1:
                node = s1.pop()
                level.append(node.val)
                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)
            if level:
                result.append(level)
            level = []
            while s2:
                node = s2.pop()
                level.append(node.val)
                if node.right:
                    s1.append(node.right)
                if node.left:
                    s1.append(node.left)
            if level:
                result.append(level)
            level = []
        return result
