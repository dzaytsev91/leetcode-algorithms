# hints
# put nodes in stack with current max val
# and increase count every time we found node with equals or bigger value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res
        node = root
        stack = [(node, node.val)]
        while stack:
            node, tmp_max = stack.pop()
            if node.val >= tmp_max:
                res += 1
                tmp_max = node.val
            if node.right:
                stack.append([node.right, tmp_max])
            if node.left:
                stack.append([node.left, tmp_max])

        return res


