# idea: go through all possible steps until we hit the wall
# than recursively call on each i,j, dont forget to check array boarders
# each time, remember all seen cells


class Solution:
    def hasPath(self, maze, start, destination):
        m, n, seen = len(maze), len(maze[0]), set()
        def dfs(i, j):
            if destination == [i, j]:
                return True

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x = i
                y = j
                while 0 <= x+dx < m and 0 <= y+dy < n and not maze[x+dx][y+dy]:
                    x += dx
                    y += dy
                if (x, y) not in seen:
                    seen.add((x, y))
                    if dfs(x, y):
                        return True
            return False
        return dfs(start[0], start[1])
