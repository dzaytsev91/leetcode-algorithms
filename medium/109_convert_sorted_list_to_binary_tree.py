# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.constructTree(nums, 0, len(nums)-1)

    def constructTree(self, nums, left, right):
        if left > right:
            return
        midpoint = left + (right-left) // 2
        root = TreeNode(val=nums[midpoint])
        root.right = self.constructTree(nums, midpoint+1, right)
        root.left = self.constructTree(nums, left, midpoint-1)
        return root
