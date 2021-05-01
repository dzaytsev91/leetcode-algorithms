# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, [], 1)]
        while stack:
            node, path, seq_count = stack.pop()
            if node is None:
                continue
            if path and node.val-1 == path[-1]:
                seq_count += 1
            else:
                seq_count = 1
            stack.append([node.right, path + [node.val], seq_count])
            stack.append([node.left, path + [node.val], seq_count])
            result = max(result, seq_count)
        return result
