from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) < 2:
            return 0

        for index in range(len(prices)):
            if index == len(prices) - 1:
                return max_profit

            if prices[index] < prices[index + 1]:
                max_profit += prices[index + 1] - prices[index]
        return max_profit
