from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> \
    List[int]:
        if numCourses < 1:
            return []
        if numCourses == 1 and not prerequisites:
            return [0]

        todo = {x: set() for x in range(numCourses)}
        reqs = defaultdict(set)
        res = []

        for course, req in prerequisites:
            todo[course].add(req)
            reqs[req].add(course)

        stack = []
        for val in todo:
            if len(todo[val]) == 0:
                stack.append(val)

        while stack:
            course = stack.pop(0)
            for value in reqs[course]:
                todo[value].remove(course)
                if len(todo[value]) == 0:
                    stack.append(value)
            todo.pop(course)
            res.append(course)

        if len(todo) > 0:
            return []

        return res
