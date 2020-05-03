from collections import defaultdict


class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return []
        levels = defaultdict(list)
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            levels[level].append(node.val)
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        result = []
        for level in levels:
            result.append(sum(levels[level]) / len(levels[level]))
        return result
