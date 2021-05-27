# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        tmp = result
        carry = False
        while l1 or l2:
            tmp_result = 0
            if l1:
                tmp_result += l1.val
                l1 = l1.next
            if l2:
                tmp_result += l2.val
                l2 = l2.next

            if carry:
                tmp_result += 1

            if tmp_result > 9:
                carry = True
                tmp_result -= 10
            else:
                carry = False

            tmp.next = ListNode(val=tmp_result)
            tmp = tmp.next

        if carry:
            tmp.next = ListNode(val=1)

        return result.next
