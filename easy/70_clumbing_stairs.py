class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        res = [0]*n
        res[0], res[1] = 1, 2
        for index in range(2, n):
            res[index] = res[index - 1] + res[index - 2]
        return res[-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
