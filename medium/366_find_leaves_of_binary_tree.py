# idea: traverse tree using DFS and store parent values for each node to dict
# and add leaves to list than pop leaves, delete parent connection and
# check if parent become leave, if yes add to list


# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        data = defaultdict()
        q = []
        result = []
        self.dfs(root, data, q)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                parent_node = data.get(node)
                if parent_node and parent_node.left == node:
                    parent_node.left = None
                if parent_node and parent_node.right == node:
                    parent_node.right = None

                if parent_node and not parent_node.left and not \
                        parent_node.right:
                    q.append(parent_node)
            result.append(level)
        return result

    def dfs(self, root, data, q):
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.right and not node.left:
                q.append(node)

            if node.right:
                data[node.right] = node
                stack.append(node.right)
            if node.left:
                data[node.left] = node
                stack.append(node.left)
