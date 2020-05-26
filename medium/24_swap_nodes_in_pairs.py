# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        temp = ListNode(0)
        temp.next = head
        current = temp
        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            current.next = second

            second.next = first

            current.next.next = first
            current = current.next.next

        return temp.next
