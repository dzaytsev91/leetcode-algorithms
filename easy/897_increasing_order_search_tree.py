# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        resp = TreeNode()
        tmp = resp

        def dfs(node, tmp):
            if node.left:
                tmp = dfs(node.left, tmp)

            new_node = TreeNode(val=node.val)
            tmp.right = new_node
            tmp = tmp.right

            if node.right:
                tmp = dfs(node.right, tmp)
            return tmp

        dfs(root, tmp)
        return resp.right

