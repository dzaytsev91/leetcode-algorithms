# idea: recursive call with memoization


class Solution:
    def __init__(self):
        self.cache = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n - 1] = self.tribonacci(n - 1)
        self.cache[n - 2] = self.tribonacci(n - 2)
        self.cache[n - 3] = self.tribonacci(n - 3)
        return self.cache[n - 1] + self.cache[n - 2] + self.cache[n - 3]
