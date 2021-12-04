# idea: do dfs but put right nodes at first
# my solution is not the best one, but it was easier for me to remember
# add ideal solution below


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1, True]]
        result = {"lvl": 0, "node": None}
        while stack:
            node, lvl, is_left = stack.pop()

            if lvl == result["lvl"] and is_left:
                result["lvl"] = lvl
                result["node"] = node

            if lvl > result["lvl"]:
                result["lvl"] = lvl
                result["node"] = node

            if node.right:
                stack.append([node.right, lvl + 1, False])

            if node.left:
                stack.append([node.left, lvl + 1, True])

        return result["node"].val

# class Solution:
#     def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         stack = [root]
#         result = None
#         while stack:
#             node = stack.pop()
#             result = node.val
#
#             if node.right:
#                 stack.insert(0, node.right)
#
#             if node.left:
#                 stack.insert(0, node.left)
#         return result
