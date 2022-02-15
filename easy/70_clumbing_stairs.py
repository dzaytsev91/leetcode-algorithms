class Solution:
    def __init__(self):
        self.cache = {1: 1, 2: 2, 3: 3}

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n - 1] = self.climbStairs(n - 1)
        self.cache[n - 2] = self.climbStairs(n - 2)
        return self.cache[n - 1] + self.cache[n - 2]
