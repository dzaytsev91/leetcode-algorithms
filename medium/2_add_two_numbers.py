# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next\


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return [0]

        result = ListNode()
        tmp = result
        reminder = 0

        while l1 or l2:
            total_sum = 0
            if l1:
                total_sum += l1.val
                l1 = l1.next
            if l2:
                total_sum += l2.val
                l2 = l2.next

            total_sum += reminder

            if total_sum > 9:
                reminder = 1
                new_node = ListNode(val=total_sum - 10)
            else:
                new_node = ListNode(val=total_sum)
                reminder = 0

            tmp.next = new_node
            tmp = new_node

        if reminder > 0:
            new_node = ListNode(val=reminder)
            tmp.next = new_node

        return result.next


