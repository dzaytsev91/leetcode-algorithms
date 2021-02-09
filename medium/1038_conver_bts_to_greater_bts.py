# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        data = {}
        stack = [root]
        while stack:
            node = stack.pop()

            data[node.val] = node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        stack = [root]
        while stack:
            node = stack.pop()
            for key in data:
                if node.val > key:
                    data[key] += node.val

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        stack = [root]
        print(data)
        while stack:
            node = stack.pop()
            node.val = data[node.val]
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return root


