from typing import List


class Solution:
    def dfs(self, grid, i,j):
        if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[i])-1 or grid[i][j] != 1:
            return 0

        self.islands += 1
        grid[i][j] = 0

        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.islands = 0
                self.dfs(grid, i, j)
                result = max(result, self.islands)
        return result
