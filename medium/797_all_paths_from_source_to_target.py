from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        if not graph:
            return []

        result = []
        stack = []
        for element in graph[0]:
            stack.append([element, [0]])

        while stack:
            item, path = stack.pop()
            if item == len(graph) - 1:
                path.append(item)
                result.append(path)
                continue

            for element in graph[item]:
                new_path = path[::]
                new_path.append(item)
                stack.append([element, new_path])
        return result

