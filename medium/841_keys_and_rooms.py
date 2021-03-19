from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = []
        stack = [0]
        while stack:
            key = stack.pop()
            if key in visited:
                continue
            keys = rooms[key]
            for k in keys:
                stack.append(k)

            visited.append(key)

        for index in range(len(rooms)):
            if index not in visited:
                return False

        return True
