# idea: memorize recursive call, move from end to start and get min() from
# two possibilities

from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def min_steps(index):
            if index <= 1:
                return 0
            if index in cache:
                return cache[index]

            one_step = cost[index - 1] + min_steps(index - 1)
            second_step = cost[index - 2] + min_steps(index - 2)
            cache[index] = min(one_step, second_step)
            return cache[index]

        return min_steps(len(cost))
