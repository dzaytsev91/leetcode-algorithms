# idea: traverse from p to root and store the path
# traverse from q to root and check if q.parent in path if yes return q


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def dfs(self, root):
        path = []
        stack = [root]
        while stack:
            node = stack.pop()
            path.append(node)
            if not node.parent:
                return path
            stack.append(node.parent)

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path = self.dfs(p)
        while q not in p_path:
            q = q.parent
        return q
