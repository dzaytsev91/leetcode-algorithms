from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        return self.constructTree(nums, 0, len(nums) - 1)

    def constructTree(self, nums, left, right):
        if left > right:
            return
        midpoint = left + (right - left) // 2
        root = TreeNode(val=nums[midpoint])
        root.right = self.constructTree(nums, midpoint + 1, right)
        root.left = self.constructTree(nums, left, midpoint - 1)
        return root

