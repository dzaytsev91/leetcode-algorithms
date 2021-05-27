from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        last_price = prices[0]
        for index in range(1, len(prices)):
            if last_price < prices[index]:
                result += prices[index] - last_price
            last_price = prices[index]
        return result
