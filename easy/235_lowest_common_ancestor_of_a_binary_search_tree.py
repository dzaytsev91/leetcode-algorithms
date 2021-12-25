# idea: do dfs with stack and check when split occurs
# split is when q is greater than node and p not
# either q is lower than node and p not
# space complexity O(1)
# time complexity O(log n)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        while stack:
            node = stack.pop()
            if p.val > node.val < q.val:
                stack.append(node.right)
            elif p.val < node.val > q.val:
                stack.append(node.left)
            else:
                return node
