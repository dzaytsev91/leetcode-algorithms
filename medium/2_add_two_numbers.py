# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        temp = result
        carry = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            current_sum = l1_val + l2_val + carry
            carry = current_sum // 10
            last_digit = current_sum % 10

            temp.next = ListNode(val=last_digit)

            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            node = ListNode(val=1)
            temp.next = node

        return result.next

