from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_val = 0, float('inf')
        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price - min_val)
        return max_profit
