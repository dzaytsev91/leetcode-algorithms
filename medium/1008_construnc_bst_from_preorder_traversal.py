from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(val=preorder.pop(0))
        while preorder:
            current_node = root
            val = preorder.pop(0)
            node = TreeNode(val=val)

            while True:
                if val < current_node.val:
                    if not current_node.left:
                        current_node.left = node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = node
                        break
                    else:
                        current_node = current_node.right
        return root
