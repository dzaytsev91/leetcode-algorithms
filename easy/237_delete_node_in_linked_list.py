class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        while node.next != None:
            node.val = node.next.val
            cur = node
            node = node.next
        cur.next = None
