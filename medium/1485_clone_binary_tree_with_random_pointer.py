class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random
    

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return root
        stack = [root]
        visited = {root: NodeCopy(val=root.val)}
        while stack:
            node = stack.pop()
            if node not in visited:
                visited[node] = NodeCopy(val=node.val)
            if node.left and node.left not in visited:
                visited[node.left] = NodeCopy(val=node.left.val)
                stack.append(node.left)
            if node.right and node.right not in visited:
                visited[node.right] = NodeCopy(val=node.right.val)
                stack.append(node.right)
            if node.random and node.random not in visited:
                visited[node.random] = NodeCopy(val=node.random.val)
                stack.append(node.random)

            if node.left:
                visited[node].left = visited[node.left]
            if node.right:
                visited[node].right = visited[node.right]
            if node.random:
                visited[node].random = visited[node.random]
        return visited[root]

