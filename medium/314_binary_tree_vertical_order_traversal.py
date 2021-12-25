# idea: do dfs, put current coordinate and node,
# but put left node first and pop most left element firts from stack
# than add coordinate and node to dict
# than sort dict and return values


from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0)]
        data = defaultdict(list)
        while stack:
            node, x = stack.pop(0)
            data[x].append(node.val)
            if node.left:
                stack.append([node.left, x - 1])
            if node.right:
                stack.append([node.right, x + 1])

        return [data[i] for i in sorted(data)]
