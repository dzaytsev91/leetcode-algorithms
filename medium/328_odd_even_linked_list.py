# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddHead = ListNode()
        evenHead = ListNode()
        new_odd_head = oddHead
        new_even_head = evenHead
        index = 1
        while head:
            if index % 2 == 0:
                new_even_head.next = head
                new_even_head = new_even_head.next
            else:
                new_odd_head.next = head
                new_odd_head = new_odd_head.next

            head = head.next
            index += 1

        new_even_head.next = None

        new_odd_head.next = evenHead.next

        return oddHead.next
