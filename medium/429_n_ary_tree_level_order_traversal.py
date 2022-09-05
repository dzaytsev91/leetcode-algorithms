"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        stack = [(root,)]
        while stack:
            new_level = []
            local_result = []
            nodes = stack.pop()
            if not nodes:
                continue
            for node in nodes:
                local_result.append(node.val)
                for child in node.children:
                    new_level.append(child)
            result.append(local_result)
            stack.append(new_level)
        return result
