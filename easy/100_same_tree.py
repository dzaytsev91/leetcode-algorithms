# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        first_tree = []
        second_tree = []
        stack = [p]
        while stack:
            node = stack.pop()
            if node:
                first_tree.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                first_tree.append(None)

        stack = [q]
        while stack:
            node = stack.pop()
            if node:
                second_tree.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                second_tree.append(None)

        return first_tree == second_tree
