# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        stack = []
        result = [0] * len(nums)
        for index in range(len(nums)):
            while stack and nums[stack[len(stack) - 1]] < nums[index]:
                result[stack.pop()] = nums[index]

            stack.append(index)
        return result
