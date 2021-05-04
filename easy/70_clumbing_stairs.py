class Solution:

    def climbStairs(self, n: int) -> int:
        cache = {}

        def rec(n):
            if cache.get(n):
                return cache.get(n)
            if n == 0 or n == 1:
                return 1
            result = rec(n - 1) + rec(n - 2)
            cache[n] = result
            return result

        return rec(n)
