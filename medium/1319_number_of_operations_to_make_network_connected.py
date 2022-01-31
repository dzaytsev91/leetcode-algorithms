# idea: make for loop on each node check if its not in visited
# if not make dfs and add to visited all visited nodes during dfs
# count all times that you have to run dfs -1


import collections
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        data = {}
        for node in range(n):
            data[node] = []

        for j, k in connections:
            data[j].append(k)
            data[k].append(j)
        visited = set()

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for req in data[node]:
                    dfs(req)

        not_connected_nodes = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                not_connected_nodes += 1
        return not_connected_nodes - 1
