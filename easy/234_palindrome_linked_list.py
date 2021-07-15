# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        left = 0
        right = len(values) - 1
        while right > left:
            if values[right] != values[left]:
                return False
            left += 1
            right -= 1
        return True
