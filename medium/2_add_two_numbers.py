# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_number = []
        second_number = []
        result_val = []
        first_val = 0
        second_val = 0

        while l1:
            first_number.insert(0, str(l1.val))
            l1 = l1.next
        while l2:
            second_number.insert(0, str(l2.val))
            l2 = l2.next

        if first_number:
            first_val = int("".join(first_number))
        if second_number:
            second_val = int("".join(second_number))

        for val in str(first_val + second_val):
            result_val.insert(0, val)

        result = ListNode(0)
        temp = result
        for num in result_val:
            node = ListNode(val=int(num))
            temp.next = node
            temp = node

        return result.next
