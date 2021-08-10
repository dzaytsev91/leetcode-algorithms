class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = []
        for row in range(m):
            matrix.append([1] * n)

        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]
        return matrix[m - 1][n - 1]
