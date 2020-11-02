class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1

        dp = [[0]*n for x in range(m)]

        for cell in range(1, m):
            dp[cell][0] = 1

        for cell in range(1, n):
            dp[0][cell] = 1

        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[-1][-1]
