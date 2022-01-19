# idea: put all prerequisites in dict {<course>: [<array of prereqs>]}
# than go for each course and try to run dfs to complete it
# check if cycle exists, this is the only possible error
# time complexity: O(E+V) where E = number of dependencies and
# V = number of courses
# space complexity: O(E+V)
# important note: remember adding nodes to result in right place,
# right after you are sure it can be done

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> \
    List[int]:
        prereqs = {}
        for course in range(numCourses):
            prereqs[course] = []

        for course, req in prerequisites:
            prereqs[course].append(req)

        visited = set()
        cycle = set()
        result = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for pre in prereqs[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return result
