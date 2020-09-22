# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = [root]
        result_sum = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            stack.append(node.left)
            stack.append(node.right)
            if node.val % 2 == 0:
                if node.left:
                    child = node.left
                    if child.left:
                        result_sum += child.left.val
                    if child.right:
                        result_sum += child.right.val
                if node.right:
                    child = node.right
                    if child.left:
                        result_sum += child.left.val
                    if child.right:
                        result_sum += child.right.val
        return result_sum

