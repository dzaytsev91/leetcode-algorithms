# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        nums = []
        stack = [head]
        while stack:
            node = stack.pop()
            nums.append(node.val)

            if node.next:
                stack.append(node.next)

        nums_length = len(nums)
        if nums_length < 2:
            return head

        nums[k-1], nums[nums_length-k] = nums[nums_length-k], nums[k-1]

        new_head = ListNode()
        tmp_head = new_head
        while nums:
            val = nums.pop(0)
            new_node = ListNode(val=val)
            tmp_head.next = new_node
            tmp_head = new_node
        return new_head.next

