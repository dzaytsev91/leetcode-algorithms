# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        resp = Node(x=0)
        tmp_orig = head
        prev = resp
        data = {}

        while tmp_orig:
            new_node = Node(x=tmp_orig.val)
            prev.next = new_node
            prev = new_node
            data[tmp_orig] = new_node
            tmp_orig = tmp_orig.next

        tmp_orig = head
        tmp_new = resp.next
        while tmp_orig:
            if tmp_orig.random:
                tmp_new.random = data[tmp_orig.random]
            tmp_orig = tmp_orig.next
            tmp_new = tmp_new.next

        return resp.next
