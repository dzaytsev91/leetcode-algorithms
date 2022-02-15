# idea: recursive call with memoization

class Solution:
    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n-1] = self.fib(n-1)
        self.cache[n-2] = self.fib(n-2)
        return self.cache[n-1] + self.cache[n-2]
