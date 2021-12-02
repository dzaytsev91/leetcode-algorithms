# idea: convert bst to graph than bfs with levels and
# add all nodes with needed values


# Definition for a binary tree node.
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        data = defaultdict(list)
        visited, stack, res = set(), [], []
        self.convert_to_graph(root, data, None)

        stack.append([target, 0])
        while stack:
            node, level = stack.pop(0)
            visited.add(node)

            if level == k:
                res.append(node.val)

            for neighbor in data[node]:
                if neighbor not in visited:
                    stack.append([neighbor, level + 1])
        return res

    def convert_to_graph(self, node, data, parent):
        if node is None:
            return

        if parent is not None:
            data[node].append(parent)

        if node.right:
            data[node].append(node.right)
            self.convert_to_graph(node.right, data, node)

        if node.left:
            data[node].append(node.left)
            self.convert_to_graph(node.left, data, node)

        return

