# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        result = ListNode(val=0)
        result.next = head
        fast, slow = result, result
        for idx in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return result.next
