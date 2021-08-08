from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = {}
        result = 0

        def dfs(index):
            stack = [index]
            visited[index] = True
            while stack:
                node = stack.pop()
                for node2 in range(len(isConnected)):
                    if isConnected[node][node2] == 1 and not visited.get(
                            node2):
                        stack.append(node2)
                        visited[node2] = True

        for indx in range(len(isConnected)):
            if indx not in visited:
                dfs(indx)
                result += 1
        return result
