# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode,
                      target: TreeNode) -> TreeNode:
        stack = [original]
        clone_stack = [cloned]
        while stack:
            root = stack.pop()
            cloned_root = clone_stack.pop()
            if root == target:
                return cloned_root
            if root:
                stack.append(root.right)
                stack.append(root.left)

                clone_stack.append(cloned_root.right)
                clone_stack.append(cloned_root.left)
