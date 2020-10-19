from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        todo = dict()
        graph = defaultdict(set)
        stack = []

        for key, val in prerequisites:
            if key not in todo:
                todo[key] = set()
            if val not in todo:
                todo[val] = set()

            todo[key].add(val)
            graph[val].add(key)

        for key in todo:
            if len(todo[key]) == 0:
                stack.append(key)

        while stack:
            node = stack.pop(0)

            for value in graph[node]:
                todo[value].remove(node)

                if len(todo[value]) == 0:
                    stack.append(value)

            todo.pop(node)

        return not todo

