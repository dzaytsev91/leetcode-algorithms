from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def helper(self, root, res):
        if root:
            res.append(root.val)
            for child in root.children:
                self.helper(child, res)
        return res

    def preorder(self, root: 'Node') -> List[int]:
        res = []
        return self.helper(root, res)
