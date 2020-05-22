# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur_val = head.val
        last_head = head
        start_head = head
        while head:
            if head.val != cur_val:
                last_head.next = head
                last_head = head
            if not head.next:
                last_head.next = None
                return start_head
            cur_val = head.val

            head = head.next

        return start_head
