from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0

        cache = {}

        def dp(amount):
            if amount in cache:
                return cache[amount]
            if amount == 0:
                return 0

            tmp = []
            for coin in coins:
                if amount - coin >= 0:
                    tmp.append(dp(amount - coin))
                else:
                    tmp.append(float('inf'))

            min_coins = min(tmp) + 1
            cache[amount] = min_coins
            return min_coins

        result = dp(amount)
        if result != float('inf'):
            return result

        return -1
