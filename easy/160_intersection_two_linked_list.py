# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA and not headB:
            return
        a_pointer = headA
        b_pointer = headB
        while a_pointer != b_pointer:
            if not a_pointer:
                a_pointer = headB
            else:
                a_pointer = a_pointer.next

            if not b_pointer:
                b_pointer = headA
            else:
                b_pointer = b_pointer.next
        return a_pointer
