from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = defaultdict(set)
        for start, end in edges:
            components[start].add(end)
            components[end].add(start)

        seen = set()

        def dfs(node):
            if node not in seen:
                seen.add(node)
                for q in components[node]:
                    dfs(q)

        result = 0
        for index in range(n):
            if index not in seen:
                dfs(index)
                result += 1
        return result
