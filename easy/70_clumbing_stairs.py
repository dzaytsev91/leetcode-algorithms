class Solution:
    def __init__(self):
        self.cache = {1: 1, 2: 2}

    def count_steps(self, n):
        if self.cache.get(n):
            return self.cache.get(n)
        if n == 0 or n == 1:
            return 1

        result = self.count_steps(n - 1) + self.count_steps(n - 2)
        self.cache[n] = result
        return result

    def climbStairs(self, n: int) -> int:
        return self.count_steps(n)
