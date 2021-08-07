class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        stack = [head]
        visited = {head: Node(head.val)}
        while stack:
            node = stack.pop()
            if node not in visited:
                visited[node] = Node(node.val)
            if node.next and node.next not in visited:
                visited[node.next] = Node(node.next.val)
                stack.append(node.next)

            if node.random and node.random not in visited:
                visited[node.random] = Node(node.random.val)
                stack.append(node.random)
            if node.next:
                visited[node].next = visited[node.next]
            if node.random:
                visited[node].random = visited[node.random]
        return visited[head]
