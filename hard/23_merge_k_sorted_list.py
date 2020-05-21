# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        start_head = None
        cur_head = None
        stack = []
        for row in lists:
            while row:
                stack.append(row.val)
                row = row.next

        stack.sort()

        while stack:
            if not start_head:
                start_head = ListNode(val=stack.pop(0))
                cur_head = start_head
            else:
                new_head = ListNode(val=stack.pop(0))
                cur_head.next = new_head
                cur_head = new_head
        return start_head
