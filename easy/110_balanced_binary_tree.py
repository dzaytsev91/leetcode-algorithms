# hint
# recursively count depth for right and than for left and compare


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(node):
            if node is None:
                return 0
            right = check(node.right)
            left = check(node.left)
            if right == -1 or left == -1 or abs(right - left) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


