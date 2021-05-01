from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        stack = [(root, 0, [])]
        while stack:
            node, current_sum, current_path = stack.pop()
            if node is None:
                continue

            if current_sum + node.val == targetSum and not node.right and \
                    not node.left:
                result.append(current_path + [node.val])

            stack.append([node.right, current_sum + node.val,
                          current_path + [node.val]])
            stack.append(
                [node.left, current_sum + node.val, current_path + [node.val]])
        return result
