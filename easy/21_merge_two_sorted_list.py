# repeat


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(x=0)
        prev_head = head
        while True:
            if not l1 and not l2:
                return head.next
            if not l1:
                prev_head.next = l2
                return head.next
            if not l2:
                prev_head.next = l1
                return head.next

            if l1.val < l2.val:
                new_node = ListNode(l1.val)
                prev_head.next = new_node
                l1 = l1.next
                prev_head = prev_head.next
            else:
                new_node = ListNode(l2.val)
                prev_head.next = new_node
                l2 = l2.next
                prev_head = prev_head.next


if __name__ == '__main__':
    l3 = ListNode(x=4)
    l2 = ListNode(x=2)
    l2.next = l3
    l1 = ListNode(x=1)
    l1.next = l2

    l6 = ListNode(x=4)
    l7 = ListNode(x=3)
    l7.next = l6
    l8 = ListNode(x=1)
    l8.next = l7

    res = Solution().mergeTwoLists(l1, l8)
    import ipdb; ipdb.set_trace();
    print(123)


