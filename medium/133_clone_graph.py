# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        stack = [node]
        visited = {node: Node(node.val, [])}
        while stack:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
