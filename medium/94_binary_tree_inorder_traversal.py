# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if root == None:
            return result

        while stack or root != None:
            while root != None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

