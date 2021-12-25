# idea: problem is very similar to medium vertical traversal but the one thing
# we have to sort the nested array with row value
# the idea is to add row + val to nested array and sort them
# than loop throught and call sort for every nested array as well and
# add second value from this array to result


from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        data = defaultdict(list)
        stack = [(root, 0, 0)]
        while stack:
            node, row, col = stack.pop()
            data[col].append([abs(row), node.val])
            if node.left:
                stack.append([node.left, row + 1, col - 1])
            if node.right:
                stack.append([node.right, row + 1, col + 1])

        for key in sorted(data.keys()):
            result.append([v[1] for v in sorted(data[key])])

        return result
