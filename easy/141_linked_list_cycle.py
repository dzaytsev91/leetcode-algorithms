# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        nums = set()
        while head:
            if head in nums:
                return True
            nums.add(head)
            head = head.next
        return False


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    l3 = ListNode(3)
    l2.next = l3
    l3.next = l2
    solution = Solution()

    assert solution.hasCycle(l1) == True
