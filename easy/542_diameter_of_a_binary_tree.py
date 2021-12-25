# idea: we cant just count the depth of left and right nodes from root
# because some inner nodes can have bigger diameter
# so we have to count diameter of each possible node recursively
# dont forget to add 1 to the result


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_diameter = 0  # stores the maximum diameter calculated

    def dfs(self, root):
        # Calculate maximum depth
        left = self.dfs(root.left) if root.left else 0
        right = self.dfs(root.right) if root.right else 0
        max_diameter = left + right
        self.max_diameter = max(self.max_diameter, max_diameter)
        return 1 + (left if left > right else right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_diameter
