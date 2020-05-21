# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        cur_head = ListNode(val=stack.pop())
        start_head = cur_head
        while stack:
            new_head = ListNode(val=stack.pop())
            cur_head.next = new_head
            cur_head = new_head
        return start_head
