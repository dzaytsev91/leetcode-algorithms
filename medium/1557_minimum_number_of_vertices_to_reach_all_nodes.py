from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes_list = [x for x in range(n)]

        visited_nodes = set()

        for k, v in edges:
            visited_nodes.add(v)

        result = []
        for val in nodes_list:
            if val not in visited_nodes:
                result.append(val)

        return result

